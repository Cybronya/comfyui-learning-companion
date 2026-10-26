---
name: unknown_workflow_sampler_clip_checkpoint_17
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8414
common_nodes: [BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, HiDreamO1PatchSeamSmoothing, KSamplerSelect, ModelNoiseScale, SamplerCustom, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】HiDream O1 comfyui官流，多图参考_2055211379967176705.json, 图片生成/文生图/Hidream-01-文生图_2055289829646192642.json, 图片生成/文生图/hidream_o1_image 文生图_2055326981159432193.json, 图片生成/文生图/hidream_o1_image_t2i_2055131118483066881.json, 图片生成/文生图/【遇见AI】HiDream O1 comfyui官流，文生图_2055167421874483202.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_17

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/【遇见AI】HiDream O1 comfyui官流，多图参考_2055211379967176705.json、图片生成/文生图/Hidream-01-文生图_2055289829646192642.json、图片生成/文生图/hidream_o1_image 文生图_2055326981159432193.json、图片生成/文生图/hidream_o1_image_t2i_2055131118483066881.json、图片生成/文生图/【遇见AI】HiDream O1 comfyui官流，文生图_2055167421874483202.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `HiDreamO1PatchSeamSmoothing`
- `KSamplerSelect`
- `ModelNoiseScale`
- `SamplerCustom`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `EmptyHiDreamO1LatentImage` —— 3/5 个有
- `AILab_QwenVL` —— 2/5 个有
- `EmptyLatentImage` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `HiDreamO1ReferenceImages` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1440 | - | 2 | 100% |
| 高度 | 2560 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1440，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 2560，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
