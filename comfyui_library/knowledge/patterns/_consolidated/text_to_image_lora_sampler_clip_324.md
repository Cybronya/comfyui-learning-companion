---
name: text_to_image_lora_sampler_clip_324
type: Text To Image
frequency: 6
level: strong
coverage: 0.888333
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX3加速版图像编辑写真级｜上传图就改不动手修_2111338389898354689.json, 图片生成/图生图/Fibo2单图多图编辑 局部重绘换背景图生图处理工具_2113706040213725186.json, 图片生成/图生图/Fibo2单图多图编辑双模式｜局部重绘换背景图生图全行_2113533013467422721.json, 图片生成/图生图/Fibo2单图编辑工作流，一张图搞定指令修图局部替换快速出图_2114465611718942722.json, 图片生成/图生图/Fibo2工作流图片修改 精修文生图处理生成工具_2113745561978490881.json, 图片生成/图生图/单图编辑FLUX3-Klein in 加速，电商图生图提速_2111607229198721025.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_324

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FLUX3加速版图像编辑写真级｜上传图就改不动手修_2111338389898354689.json、图片生成/图生图/Fibo2单图多图编辑 局部重绘换背景图生图处理工具_2113706040213725186.json、图片生成/图生图/Fibo2单图多图编辑双模式｜局部重绘换背景图生图全行_2113533013467422721.json、图片生成/图生图/Fibo2单图编辑工作流，一张图搞定指令修图局部替换快速出图_2114465611718942722.json、图片生成/图生图/Fibo2工作流图片修改 精修文生图处理生成工具_2113745561978490881.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RHFibo2EditConditioning` —— 4/6 个有
- `RHFibo2ModelLoader` —— 4/6 个有
- `RHFibo2Scheduler` —— 4/6 个有
- `RHFibo2TextEncoderLoader` —— 4/6 个有
- `Anything Everywhere3` —— 3/6 个有
- `LayerMask: PersonMaskUltra` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `Anything Everywhere` —— 2/6 个有
- `ManualSigmas` —— 2/6 个有
- `PDIMAGE_LongerSize` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `ReferenceLatent` —— 2/6 个有
- `VAEEncode` —— 2/6 个有
- `ImageConcanate` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RHFibo2KeepOutsideMask` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
