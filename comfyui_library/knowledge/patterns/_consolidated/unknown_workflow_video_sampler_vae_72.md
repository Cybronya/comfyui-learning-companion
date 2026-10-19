---
name: unknown_workflow_video_sampler_vae_72
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.845143
common_nodes: [ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/2017619701119066113.json, 视频生成/图生视频/2016868591383093249.json, 视频生成/图生视频/2017268862005284866.json, 视频生成/图生视频/2017057905576513537.json, 视频生成/图生视频/2019967934935863297.json, 视频生成/图生视频/2017514844987068418.json, 视频生成/图生视频/2026233274720325634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_72

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2017619701119066113.json、视频生成/图生视频/2016868591383093249.json、视频生成/图生视频/2017268862005284866.json、视频生成/图生视频/2017057905576513537.json、视频生成/图生视频/2019967934935863297.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `INTConstant` —— 6/7 个有
- `ImageConcatMulti` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `FlashVSRNode` —— 4/7 个有
- `Anything Everywhere` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `GetNode` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `Text` —— 1/7 个有
- `Text Multiline` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
