---
name: unknown_workflow_video_upscale_lora_25
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.939
common_nodes: [ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/返老还童图生视频_1900773672473501697.json, 视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1909470636823949313.json, 视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1992837863268216833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_25

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/返老还童图生视频_1900773672473501697.json、视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1909470636823949313.json、视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1992837863268216833.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `TextInput_` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `ReActorFaceSwap` —— 1/3 个有
- `Select Image Indices` —— 1/3 个有
- `Textbox` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
