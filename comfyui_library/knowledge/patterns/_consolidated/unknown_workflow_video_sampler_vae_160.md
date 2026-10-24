---
name: unknown_workflow_video_sampler_vae_160
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.779667
common_nodes: [ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/SkyreelV3双图参考图生视频_2019967934935863297.json, 视频生成/图生视频/SkyreelV3多主体参考图生视频_2017514844987068418.json, 视频生成/图生视频/SkyreelV3多主体参考图生视频_2026233274720325634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_160

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/SkyreelV3双图参考图生视频_2019967934935863297.json、视频生成/图生视频/SkyreelV3多主体参考图生视频_2017514844987068418.json、视频生成/图生视频/SkyreelV3多主体参考图生视频_2026233274720325634.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
