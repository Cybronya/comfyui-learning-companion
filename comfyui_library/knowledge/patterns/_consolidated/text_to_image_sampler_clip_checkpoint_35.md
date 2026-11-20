---
name: text_to_image_sampler_clip_checkpoint_35
type: Text To Image
frequency: 2
level: weak
coverage: 0.935
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, PortraitMasterBaseCharacter, PortraitMasterMakeup, PortraitMasterSkinDetails, PortraitMasterStylePose, SaveImage, Seed (rgthree), VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/ComfyUI Portrait Master Workflow_1868526829371015170.json, 数字人/数字人/【摄影】捏人-肖像大师-AIO V4版_1976982809439031297.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_35

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/ComfyUI Portrait Master Workflow_1868526829371015170.json、数字人/数字人/【摄影】捏人-肖像大师-AIO V4版_1976982809439031297.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `PortraitMasterBaseCharacter`
- `PortraitMasterMakeup`
- `PortraitMasterSkinDetails`
- `PortraitMasterStylePose`
- `SaveImage`
- `Seed (rgthree)`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPSetLastLayer` —— 1/2 个有
- `CM_SDXLResolution` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TT_img_enc` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17 | - | 2 | 24% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1020 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17，样本不足，未给区间，2 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1020，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
