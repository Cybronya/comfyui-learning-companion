---
name: unknown_workflow_video_upscale_lora_6
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.932143
common_nodes: [ImageUpscaleWithModel, Int, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1937513955088580610.json, 视频生成/图生视频/1899332733573746689.json, 视频生成/图生视频/1899672945285877762.json, 视频生成/图生视频/1899288956402356225.json, 视频生成/图生视频/1900773672473501697.json, 视频生成/文生视频/1915649803047604225.json, 视频生成/文生视频/1916330952719798273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_6

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1937513955088580610.json、视频生成/图生视频/1899332733573746689.json、视频生成/图生视频/1899672945285877762.json、视频生成/图生视频/1899288956402356225.json、视频生成/图生视频/1900773672473501697.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `Int`
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
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoEnhanceAVideo` —— 5/7 个有
- `LayerUtility: PurgeVRAM` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `Note Plus (mtb)` —— 3/7 个有
- `WanVideoTeaCache` —— 3/7 个有
- `FILM VFI` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `StringConstantMultiline` —— 2/7 个有
- `Fast Bypasser (rgthree)` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `ReActorFaceSwap` —— 1/7 个有
- `Seed Everywhere` —— 1/7 个有
- `Textbox` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
