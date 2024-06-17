using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bullet_Sponer : MonoBehaviour
{
    public GameObject bulletPrefabs; // 생성할 탄알의 원본 프리펩
    public float spawnRateMin = 0.5f; // 불릿 생성 최소 주기
    public float spawnRateMax = 3f; // 불릿 생성 최대 주기

    private Transform target;
    private float spawnRate;
    private float timeAfterSpawn;

    // Start is called before the first frame update
    void Start()
    {
        timeAfterSpawn = 0f;
        spawnRate = Random.Range(spawnRateMin, spawnRate);
        target = FindObjectOfType<Player_Controller>().transform;
    }

    // Update is called once per frame
    void Update()
    {
        timeAfterSpawn += Time.deltaTime;

        if(timeAfterSpawn >= spawnRate){
            timeAfterSpawn = 0f;

            GameObject bullet = Instantiate(bulletPrefabs, transform.position, transform.rotation);
            bullet.transform.LookAt(target);

            spawnRate = Random.Range(spawnRateMin, spawnRateMax);
        }
    }
}
