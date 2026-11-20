---
name: unknown_workflow_video_sampler_vae_174
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.925667
common_nodes: [CLIPVisionLoader, CreateVideo, ImageResizeKJv2, JjkText, LoadImage, SaveVideo, VHS_LoadVideo, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoImageResizeToClosest, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/SCAIL2动作迁移-免骨架工作流_2101624513002819586.json, 平台全量/SCAIL2动作迁移-免骨架工作流_2100056752506105857.json, 平台全量/SCAIL2动作迁移-免骨架工作流_2100137506623803394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_174

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SCAIL2动作迁移-免骨架工作流_2101624513002819586.json、平台全量/SCAIL2动作迁移-免骨架工作流_2100056752506105857.json、平台全量/SCAIL2动作迁移-免骨架工作流_2100137506623803394.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `CreateVideo`
- `ImageResizeKJv2`
- `JjkText`
- `LoadImage`
- `SaveVideo`
- `VHS_LoadVideo`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoImageResizeToClosest`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
