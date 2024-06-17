using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player_Controller : MonoBehaviour
{
    public Rigidbody rigidbody;

    public float moveSpeed;

    // Start is called before the first frame update
    void Start()
    {
        rigidbody = gameObject.GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        // if (Input.GetKey(KeyCode.UpArrow)){
        //     rigidbody.AddForce(0f, 0f, moveSpeed);
        // }
        // if (Input.GetKey(KeyCode.DownArrow)){
        //     rigidbody.AddForce(0f, 0f, -moveSpeed);
        // }
        // if (Input.GetKey(KeyCode.RightArrow)){
        //     rigidbody.AddForce(moveSpeed, 0f, 0f);
        // }
        // if (Input.GetKey(KeyCode.LeftArrow)){
        //     rigidbody.AddForce(-moveSpeed, 0f, 0f);
        // }
        
        // 위 코드랑 같다.
        float xInput = Input.GetAxis("Horizontal");
        float zInput = Input.GetAxis("Vertical");
        
        float xSpeed = xInput * moveSpeed;
        float zSpeed = zInput * moveSpeed;
        

        Vector3 myVelocity = new Vector3(xSpeed, 0f, zSpeed);
        rigidbody.velocity = myVelocity;
    }
    public void Die(){
        gameObject.SetActive(false);
        

    }
}
