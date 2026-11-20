---
name: image_to_image_sampler_clip_unet_28
type: Image To Image
frequency: 13
level: strong
coverage: 0.896538
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/全能视频S 突破真人图像加载hd高清版_1976967687794499585.json, 平台全量/最强去除水印_1938912006843850753.json, 视频生成/图生视频/全能视频S 真人图片带货视频高清修复版支持hd高清竖版横板seedvr2二次高清视频_1979019890944282626.json, 视频生成/图生视频/全能视频S 真人版丨突破真人限制高清图生视频！！！_1980175140845686785.json, 视频生成/图生视频/全能视频S 真人版带货版突破真人限制无水印带货视频直出_1981394099058155522.json, 视频生成/图生视频/全能视频S 真人突破高清修复版支持hd高清竖版横板_1976662868592676865.json, 视频生成/图生视频/全能视频S+真人突破高清修复版支持hd高清竖版横板_1987128422977703937.json, 视频生成/图生视频/全能视频S2 图生视频（破除真人限制）_1983836311914258433.json, 视频生成/图生视频/全能视频S真人图片直出视频二次高清版图生视频支持竖版9_16和横版16_9及hd版真人视频_1974791386690097154.json, 视频生成/图生视频/全能视频S真人图片直出视频二次高清版图生视频支持竖版9_16和横版16_9及hd版真人视频_1977406898737684481.json, 视频生成/图生视频/顶配 全能视频S 真人突破版hd高清竖版横板_1976679775987290113.json, 视频生成/文生视频/全能视频S  突破真人_1987944719135256577.json, 视频生成/文生视频/全能视频S 突破真人，高清版_1984183574075211778.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_28

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/全能视频S 突破真人图像加载hd高清版_1976967687794499585.json、平台全量/最强去除水印_1938912006843850753.json、视频生成/图生视频/全能视频S 真人图片带货视频高清修复版支持hd高清竖版横板seedvr2二次高清视频_1979019890944282626.json、视频生成/图生视频/全能视频S 真人版丨突破真人限制高清图生视频！！！_1980175140845686785.json、视频生成/图生视频/全能视频S 真人版带货版突破真人限制无水印带货视频直出_1981394099058155522.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 12/13 个有
- `LoraLoaderModelOnly` —— 12/13 个有
- `RH_Sora2_I2V` —— 12/13 个有
- `SaveImage` —— 12/13 个有
- `SaveVideo` —— 12/13 个有
- `CR Prompt Text` —— 11/13 个有
- `easy cleanGpuUsed` —— 11/13 个有
- `easy showAnything` —— 10/13 个有
- `SeedVR2` —— 7/13 个有
- `VHS_LoadVideoPath` —— 7/13 个有
- `VHS_VideoCombine` —— 7/13 个有
- `Bookmark (rgthree)` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `SeedVR2GGUF` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 12 - 30 | 13 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | beta | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 12 - 30，13 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
