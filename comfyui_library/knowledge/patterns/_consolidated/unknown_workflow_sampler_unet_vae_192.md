---
name: unknown_workflow_sampler_unet_vae_192
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.952143
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image-Edit一无偏移人物一致编辑_1968878360459923457.json, 图片生成/图生图/【三图】多人场景融合-Qwan-Edit2509图像编辑_1972103949195145218.json, 图片生成/图生图/千问-模特快速换装协作工作流_1994286662249283585.json, 平台全量/Pose姿势+服装3图参考-千问Edit2509图像编辑_1970530281180569602.json, 平台全量/Pose姿势+服装3图参考-千问Edit2509图像编辑_1970838526155726850.json, 平台全量/Qwen-Edit2509 图像编辑 Pose姿势参考 V1.0_1971098337367756801.json, 平台全量/QwenEdit2509图像编辑-换装换姿势_1985997581199257602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_192

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit一无偏移人物一致编辑_1968878360459923457.json、图片生成/图生图/【三图】多人场景融合-Qwan-Edit2509图像编辑_1972103949195145218.json、图片生成/图生图/千问-模特快速换装协作工作流_1994286662249283585.json、平台全量/Pose姿势+服装3图参考-千问Edit2509图像编辑_1970530281180569602.json、平台全量/Pose姿势+服装3图参考-千问Edit2509图像编辑_1970838526155726850.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `ImageStitch` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `AIO_Preprocessor` —— 5/7 个有
- `EmptyLatentImage` —— 4/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `TextEncodeQwenImageEditPlus` —— 4/7 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 4/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `ImageScaleDownToSize` —— 2/7 个有
- `CLIPTextEncode` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 7 | 81% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | beta57 | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 beta57，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
