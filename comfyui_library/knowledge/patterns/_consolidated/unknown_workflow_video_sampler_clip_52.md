---
name: unknown_workflow_video_sampler_clip_52
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.843
common_nodes: [ImageResize+, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.1首尾帧控制_1904236934053666817.json, 图片生成/图生图/Wan官方FLF2V首尾帧工作流-KJ版_1913876729054621697.json, 视频生成/图生视频/03-04-02-WAN2.1-首尾帧生成视频-FLF2V-kijai_1989234731780804609.json, 视频生成/图生视频/03-04-05-WAN2.1-首尾帧生成视频-FUN-INP-14B-kijai_1989234577744990209.json, 视频生成/图生视频/FLF2V首尾帧-最新wan官方视频控制_1912732758077075458.json, 视频生成/图生视频/Mps奖励超稳定性Wan Fun新版首尾帧新模型自动预测视频工作流_1909949777759666177.json, 视频生成/图生视频/Vace 14B 联动 FLF2V模型优化加速版首尾帧V1_1924712621050613761.json, 视频生成/图生视频/Wan 2.1 FLF2V模型高动态优化版首尾帧V2_1912568927808094209.json, 视频生成/图生视频/Wan Fun新版首尾帧新模型自动预测视频工作流_1906320189389213697.json, 视频生成/图生视频/Wan2.1 FLF2V 首尾帧生视频_1928288843513118721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Wan2.1首尾帧控制_1904236934053666817.json、图片生成/图生图/Wan官方FLF2V首尾帧工作流-KJ版_1913876729054621697.json、视频生成/图生视频/03-04-02-WAN2.1-首尾帧生成视频-FLF2V-kijai_1989234731780804609.json、视频生成/图生视频/03-04-05-WAN2.1-首尾帧生成视频-FUN-INP-14B-kijai_1989234577744990209.json、视频生成/图生视频/FLF2V首尾帧-最新wan官方视频控制_1912732758077075458.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
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
- `GetImageSizeAndCount` —— 9/10 个有
- `AddLabel` —— 8/10 个有
- `ImageConcatMulti` —— 8/10 个有
- `WanVideoExperimentalArgs` —— 8/10 个有
- `EmptyImage` —— 7/10 个有
- `GetNode` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `WanVideoEnhanceAVideo` —— 7/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `WanVideoVRAMManagement` —— 6/10 个有
- `CLIPLoader` —— 4/10 个有
- `CLIPTextEncode` —— 4/10 个有
- `WanVideoTextEmbedBridge` —— 4/10 个有
- `CLIPVisionLoader` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `Note Plus (mtb)` —— 2/10 个有
- `Text Multiline` —— 2/10 个有
- `ImageConcanate` —— 1/10 个有
- `ImageFromBatch+` —— 1/10 个有
- `JWImageResizeByLongerSide` —— 1/10 个有
- `Primitive integer [Crystools]` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `WanVideoLoraSelect` —— 1/10 个有
- `WanVideoVACEModelSelect` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
