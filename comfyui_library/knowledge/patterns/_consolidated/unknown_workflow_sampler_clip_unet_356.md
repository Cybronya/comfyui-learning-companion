---
name: unknown_workflow_sampler_clip_unet_356
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.877
common_nodes: [CLIPTextEncode, ImageScale, LoadImage, PreviewImage, QuadrupleCLIPLoader, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, workflow>IP2PSampler]
problems: []
missing: []
members: [图片生成/图生图/图像编辑HiDream-E1.1｜图像编辑_1947605353364185089.json, 图片生成/图生图/图像编辑HiDream-E1.1｜图像风格转换_1947604199786881026.json, 图片生成/图生图/图像编辑模型HiDream-E1.1基础工作流_1945701195933732866.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_356

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图像编辑HiDream-E1.1｜图像编辑_1947605353364185089.json、图片生成/图生图/图像编辑HiDream-E1.1｜图像风格转换_1947604199786881026.json、图片生成/图生图/图像编辑模型HiDream-E1.1基础工作流_1945701195933732866.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ImageScale`
- `LoadImage`
- `PreviewImage`
- `QuadrupleCLIPLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `workflow>IP2PSampler`

**可变部分**（部分 workflow 才有）：
- `PIP_图像联结` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
