---
name: unknown_workflow_video_sampler_clip_68
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.849556
common_nodes: [AddLabel, GetImageSizeAndCount, ImageConcatMulti, ImageResize+, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.1首尾帧控制_1904236934053666817.json, 图片生成/图生图/Wan官方FLF2V首尾帧工作流-KJ版_1913876729054621697.json, 平台全量/wan2.1首尾帧官方稳定版720p_1915278424968204289.json, 平台全量/【大炮视频】wan2.1最新官方稳定首尾帧_1914979282009976834.json, 平台全量/电商首尾帧做视频 wan2.1_1915439922881167362.json, 视频生成/图生视频/FLF2V首尾帧-最新wan官方视频控制_1912732758077075458.json, 视频生成/图生视频/Mps奖励超稳定性Wan Fun新版首尾帧新模型自动预测视频工作流_1909949777759666177.json, 视频生成/图生视频/Vace 14B 联动 FLF2V模型优化加速版首尾帧V1_1924712621050613761.json, 视频生成/图生视频/Wan Fun新版首尾帧新模型自动预测视频工作流_1906320189389213697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Wan2.1首尾帧控制_1904236934053666817.json、图片生成/图生图/Wan官方FLF2V首尾帧工作流-KJ版_1913876729054621697.json、平台全量/wan2.1首尾帧官方稳定版720p_1915278424968204289.json、平台全量/【大炮视频】wan2.1最新官方稳定首尾帧_1914979282009976834.json、平台全量/电商首尾帧做视频 wan2.1_1915439922881167362.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `AddLabel`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResize+`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 8/9 个有
- `WanVideoExperimentalArgs` —— 8/9 个有
- `GetNode` —— 7/9 个有
- `SetNode` —— 7/9 个有
- `WanVideoEnhanceAVideo` —— 6/9 个有
- `WanVideoTorchCompileSettings` —— 6/9 个有
- `WanVideoVRAMManagement` —— 6/9 个有
- `CLIPLoader` —— 4/9 个有
- `CLIPTextEncode` —— 4/9 个有
- `WanVideoTextEmbedBridge` —— 4/9 个有
- `CLIPVisionLoader` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `Note Plus (mtb)` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `ImageConcanate` —— 1/9 个有
- `ImageFromBatch+` —— 1/9 个有
- `JWImageResizeByLongerSide` —— 1/9 个有
- `Primitive integer [Crystools]` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `WanVideoLoraSelect` —— 1/9 个有
- `WanVideoVACEModelSelect` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
