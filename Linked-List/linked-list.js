// Create a Node first
class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

// LinkList class will use the Node class above to start
class LinkedList {
	constructor(value) {
		const newNode = new Node(value);
		this.head = newNode;
		this.tail = this.head;
		this.length = 1;
	}

	// Push a node into the end of the the linked-list. O(1)
	push(value) {
		const newNode = new Node(value);
        
        // Check if the linked list is empty???
		if (!this.head) {
			this.head = newNode;
			this.tail = newNode;
        } else {
            // Get the tail.next first, why???
			this.tail.next = newNode;
			this.tail = newNode;
		}

		this.length++;
		return this;
	}

	// Pop a node out from the end of the linked list. O(n)
	pop() {
		// Check if the LL is empty
		if (!this.head) return undefined;

		// If length of LL > 1
		let temp = this.head
		let pre = this.head
		while (temp.next) {
			pre = temp;
			temp = temp.next;			
		}
		this.tail = pre;
		this.tail.next = null;
		this.length--

		// If the LL is empty
		if (this.length === 0) {
			this.head = null;
			this.tail = null;
		}
		return temp // temp is the item popped off
	}
}

let firstNode = new LinkedList(4);
firstNode.push(5);
firstNode.push(6);
console.log(firstNode);
