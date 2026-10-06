# VAELoader

## 节点类型

`VAELoader`

## 分类

Model Loading

## 作用

独立加载 VAE（变分自编码器），输出 VAE 给 `VAEDecode`（latent→图像）
或 `VAEEncode`（图像→latent）。

## 参数（统计自 404 个真实 workflow，630 次出现）

| 参数 | 说明 | 实测分布 |
|---|---|---|
| vae_name | VAE 文件名 | qwen_image_vae 270 / qwen_image_2.1_vae_bf16 186 / minimax_h3_audio_vae 35 / flux2-vae 32 / minimax_h3_video_vae 25 |

## 常见问题与风险

- VAE 必须与底模族配套：拿 SD1.5 的 VAE 解 Qwen Image 的 latent
  会输出纯噪声或花屏，且不报错。
- H3（视频模型）的 VAE 分 audio / video 两个，注意别接反。
- 底模内置 VAE 的工作流可不接本节点（用 Checkpoint 的 VAE 输出）。

## 可信度

Generated（2026-10-06，参数分布实测，配套规则为通行语义）TODO(待验证)
