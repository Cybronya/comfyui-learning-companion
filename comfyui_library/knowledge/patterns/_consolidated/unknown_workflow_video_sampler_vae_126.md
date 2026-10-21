---
name: unknown_workflow_video_sampler_vae_126
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9525
common_nodes: [ImageConcanate, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/1922926453934145538.json, 视频生成/图生视频/1922811355408076801.json, 视频生成/图生视频/1923223943933849602.json, 视频生成/图生视频/1923648311860129794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_126

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1922926453934145538.json、视频生成/图生视频/1922811355408076801.json、视频生成/图生视频/1923223943933849602.json、视频生成/图生视频/1923648311860129794.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageConcanate`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ImageResizeKJ` —— 3/4 个有
- `Primitive integer [Crystools]` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `StringToInt` —— 1/4 个有
- `TextSwitchCase` —— 1/4 个有
- `Trim Text _O` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
