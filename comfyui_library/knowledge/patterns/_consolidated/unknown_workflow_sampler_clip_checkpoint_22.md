---
name: unknown_workflow_sampler_clip_checkpoint_22
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8535
common_nodes: [BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, EmptyHiDreamO1LatentImage, HiDreamO1PatchSeamSmoothing, HiDreamO1ReferenceImages, KSamplerSelect, LoadImage, ModelNoiseScale, SamplerCustom, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/Hidream-o1-dev_双图编辑_2056644689247432705.json, 图片生成/图生图/Hidream-o1-双图编辑_2055265255252611073.json, 图片生成/图生图/hidream_o1_image 多图编辑_2055525591344001025.json, 图片生成/图生图/hidream_o1_image_ref_2055201577052450818.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_22

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Hidream-o1-dev_双图编辑_2056644689247432705.json、图片生成/图生图/Hidream-o1-双图编辑_2055265255252611073.json、图片生成/图生图/hidream_o1_image 多图编辑_2055525591344001025.json、图片生成/图生图/hidream_o1_image_ref_2055201577052450818.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyHiDreamO1LatentImage`
- `HiDreamO1PatchSeamSmoothing`
- `HiDreamO1ReferenceImages`
- `KSamplerSelect`
- `LoadImage`
- `ModelNoiseScale`
- `SamplerCustom`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SamplerLCM` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
