---
name: unknown_workflow_video_lora_sampler_633
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.944
common_nodes: [ColorMatch, ImageConcanate, ImageResizeKJ, LoadImage, LoadImageFromUrl, LoadWanVideoT5TextEncoder, Note Plus (mtb), PreviewImage, Primitive integer [Crystools], Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1 AccVideo vace 双图参考快速模型_1948689505176956929.json, 视频生成/图生视频/Wan2.1 VACE双图参考改进版_1948588073054535682.json, 视频生成/图生视频/Wan2.1 causvid vace 双图参考快速模型_1948684591906336769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_633

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.1 AccVideo vace 双图参考快速模型_1948689505176956929.json、视频生成/图生视频/Wan2.1 VACE双图参考改进版_1948588073054535682.json、视频生成/图生视频/Wan2.1 causvid vace 双图参考快速模型_1948684591906336769.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `ColorMatch`
- `ImageConcanate`
- `ImageResizeKJ`
- `LoadImage`
- `LoadImageFromUrl`
- `LoadWanVideoT5TextEncoder`
- `Note Plus (mtb)`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `easy imageRemBg` —— 2/3 个有
- `ImageCompositeMasked` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `RMBG` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
