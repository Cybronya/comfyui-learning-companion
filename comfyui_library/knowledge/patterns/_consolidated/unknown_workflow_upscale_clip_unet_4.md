---
name: unknown_workflow_upscale_clip_unet_4
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.796
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, Image Comparer (rgthree), LoadImage, PreviewImage, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX高清放大_1899380955994570753.json, 图片生成/图生图/SD放大工作流_1948937528062222337.json, 图片生成/图生图/🍭老许Gary：SD分块放大_2018383996949893122.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX高清放大_1899380955994570753.json、图片生成/图生图/SD放大工作流_1948937528062222337.json、图片生成/图生图/🍭老许Gary：SD分块放大_2018383996949893122.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `CR Simple Image Compare` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `LayerMask: LoadFlorence2Model` —— 1/3 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
