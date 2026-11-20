---
name: text_to_image_lora_sampler_clip_129
type: Text To Image
frequency: 12
level: strong
coverage: 0.835583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2512商业商品摄影Lora 单品棚拍电商主图生成_2098659266436616193.json, 图片生成/图生图/Qwen Image2.1图生图三套夏装｜多套服装一键试穿_2108077360229732354.json, 图片生成/图生图/Qwen Image2.1角色四视图生成 短剧通用图生图工具_2113679532476682242.json, 图片生成/图生图/Qwen Image2.1角色四视图生成短剧通用 角色设定批量产出_2109794002504601602.json, 图片生成/图生图/Qwen image 2.1姿势参考编辑 人物姿态精准控制_2109070115789692929.json, 图片生成/图生图/Remove模型Qwen Image 2.1 PE姿势编辑工作流，人物类特效擦除图生图_2106895128467173377.json, 图片生成/图生图/稳定加速版Qwen Image 2.1 PE姿势编辑 人物姿态精准控制_2109389400659554306.json, 图片生成/图生图/超级加速版Qwen Image 2.1 PE图像编辑工作流，图生图图像处理方案_2108287006626369538.json, 图片生成/文生图/Qwen Image 2.1 PE文生图工作流，人像写真海报制作文本到图像方案_2107215861605031937.json, 图片生成/文生图/Qwen Image 2.1 PE文生图工作流，高质量文本到图像生成方案_2106466665084055554.json, 图片生成/文生图/稳定加速Tao版 Qwen Image 2.1 PE文生图加图生图编辑_2104352509451137025.json, 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE文生图｜快且稳的高质量出图_2104581684481060865.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2512商业商品摄影Lora 单品棚拍电商主图生成_2098659266436616193.json、图片生成/图生图/Qwen Image2.1图生图三套夏装｜多套服装一键试穿_2108077360229732354.json、图片生成/图生图/Qwen Image2.1角色四视图生成 短剧通用图生图工具_2113679532476682242.json、图片生成/图生图/Qwen Image2.1角色四视图生成短剧通用 角色设定批量产出_2109794002504601602.json、图片生成/图生图/Qwen image 2.1姿势参考编辑 人物姿态精准控制_2109070115789692929.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 11/12 个有
- `ResolutionSelector` —— 10/12 个有
- `CR Prompt Text` —— 9/12 个有
- `QwenImage21Cache` —— 9/12 个有
- `LoadImage` —— 8/12 个有
- `QwenImage21BlockCacheT8` —— 8/12 个有
- `QwenImage21SageAttentionT8` —— 8/12 个有
- `QwenImage21SpectrumT8` —— 8/12 个有
- `QwenPERewriteT8` —— 8/12 个有
- `ComfySwitchNode` —— 7/12 个有
- `easy cleanGpuUsed` —— 7/12 个有
- `easy showAnything` —— 7/12 个有
- `GetNode` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `Int` —— 2/12 个有
- `Seed (rgthree)` —— 2/12 个有
- `EmptySD3LatentImage` —— 1/12 个有
- `KSamplerSelect` —— 1/12 个有
- `LTXVConcatAVLatent` —— 1/12 个有
- `LTXVSeparateAVLatent` —— 1/12 个有
- `LoraLoader` —— 1/12 个有
- `ManualSigmas` —— 1/12 个有
- `SamplerCustomAdvanced` —— 1/12 个有
- `VAEEncode` —— 1/12 个有
- `VHS_VideoCombine` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
