using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bullet : MonoBehaviour
{
    public float speed;
    private Rigidbody rigidbody;
    // Start is called before the first frame update
    void Start()
    {
        rigidbody = GetComponent<Rigidbody>();
        rigidbody.velocity = transform.forward * speed;
        Destroy(gameObject, 3f);
    }

    private void OnTriggerEnter(Collider other) {
        if (other.tag == "Player"){
            Player_Controller player_Controller = other.GetComponent<Player_Controller>();

            if (player_Controller != null) {
                player_Controller.Die();
            }
        }
    }
}
