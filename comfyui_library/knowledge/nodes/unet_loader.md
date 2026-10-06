# UNETLoader

## 节点类型

`UNETLoader`

## 分类

Model Loading

## 作用

加载扩散模型主体（UNet / DiT / Flow 权重），输出 MODEL。
与 `CheckpointLoaderSimple` 的区别：只加载生成主体，不捆绑 CLIP 和 VAE，
是现代解耦式工作流（Qwen Image / Flux / Krea2 / Anima 等）的标准入口。

## 参数（统计自 404 个真实 workflow，621 次出现）

| 参数 | 说明 | 实测分布 |
|---|---|---|
| unet_name | 模型文件名 | anima_baseV10 209 / qwen_image_2.1_bf16 77 / qwen_image_2.1_int8_convrot 67 / z_image_turbo 24 / krea2_turbo_fp8 19 |
| weight_dtype | 权重精度 | 98% 为 default（按文件自身精度）；显式 fp8_e4m3fn 仅 7 次 |

## 常见问题与风险

- weight_dtype 留 default 即可；强转 fp8 省显存但可能劣化细节，
  仅在显存不够时尝试。
- 文件名里的 bf16 / int8_convrot / fp8 是量化档位，直接反映显存需求，
  挑模型先看这里。
- 输出 MODEL 后通常接 `LoraLoaderModelOnly` 或直接进采样器。

## 可信度

Generated（2026-10-06，参数分布实测，行为描述为通行语义）TODO(待验证)
