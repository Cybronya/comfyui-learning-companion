---
name: text_to_image_controlnet_sampler_clip_28
type: Text To Image
frequency: 2
level: weak
coverage: 0.8905
common_nodes: [Anything Everywhere3, CLIPTextEncode, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GoogleTranslateTextNode, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy boolean, easy cleanGpuUsed, easy int, easy positive, easy seed]
problems: []
missing: []
members: [图片生成/文生图/Kontext-双人脸融合-打造新IP新角角_1943716400794046466.json, 图片生成/文生图/图生人脸一致性角色_1941829971805683714.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Kontext-双人脸融合-打造新IP新角角_1943716400794046466.json、图片生成/文生图/图生人脸一致性角色_1941829971805683714.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GoogleTranslateTextNode`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy int`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `FaceCombine` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageSmartSharpen+` —— 1/2 个有
- `InfiniteYouApply` —— 1/2 个有
- `Int` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 976 | - | 2 | 52% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 976，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
