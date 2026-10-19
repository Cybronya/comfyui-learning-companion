---
name: image_to_image_lora_sampler_clip
type: Image To Image
frequency: 10
level: strong
coverage: 0.8933
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, RH_Sora2_I2V, ReferenceLatent, SaveImage, SaveVideo, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1979019890944282626.json, 视频生成/图生视频/1980175140845686785.json, 视频生成/图生视频/全能视频S 真人版带货版突破真人限制无水印带货视频直出_1981394099058155522.json, 视频生成/图生视频/1976662868592676865.json, 视频生成/图生视频/1987128422977703937.json, 视频生成/图生视频/全能视频S真人图片直出视频二次高清版图生视频支持竖版9_16和横版16_9及hd版真人视频_1974791386690097154.json, 视频生成/图生视频/1977406898737684481.json, 视频生成/图生视频/1976679775987290113.json, 视频生成/文生视频/全能视频S  突破真人_1987944719135256577.json, 视频生成/文生视频/全能视频S 突破真人，高清版_1984183574075211778.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1979019890944282626.json、视频生成/图生视频/1980175140845686785.json、视频生成/图生视频/全能视频S 真人版带货版突破真人限制无水印带货视频直出_1981394099058155522.json、视频生成/图生视频/1976662868592676865.json、视频生成/图生视频/1987128422977703937.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Sora2_I2V`
- `ReferenceLatent`
- `SaveImage`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `VHS_LoadVideoPath` —— 6/10 个有
- `VHS_VideoCombine` —— 6/10 个有
- `SeedVR2` —— 5/10 个有
- `Bookmark (rgthree)` —— 2/10 个有
- `SeedVR2GGUF` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
