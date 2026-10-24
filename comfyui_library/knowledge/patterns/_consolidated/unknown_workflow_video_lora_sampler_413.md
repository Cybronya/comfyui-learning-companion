---
name: unknown_workflow_video_lora_sampler_413
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8894
common_nodes: [CreateCFGScheduleFloatList, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan 2.2 FFGo 多图参考图生视频_1992952460717342721.json, 视频生成/图生视频/Wan2.2  高帧率高清｜图生视频稳定版_1950383603089891330.json, 视频生成/图生视频/Wan2.2一致性长视频_1950574501610311681.json, 视频生成/图生视频/Wan2.2图生视频-速度和质量的再一次提升_1950204585861365762.json, 视频生成/图生视频/wan2.2最好的360度旋转特效-可生成人物和物体一致性图片素材-附林黛玉写实_1986434223613636609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_413

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan 2.2 FFGo 多图参考图生视频_1992952460717342721.json、视频生成/图生视频/Wan2.2  高帧率高清｜图生视频稳定版_1950383603089891330.json、视频生成/图生视频/Wan2.2一致性长视频_1950574501610311681.json、视频生成/图生视频/Wan2.2图生视频-速度和质量的再一次提升_1950204585861365762.json、视频生成/图生视频/wan2.2最好的360度旋转特效-可生成人物和物体一致性图片素材-附林黛玉写实_1986434223613636609.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `CLIPLoader` —— 3/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `WanVideoTextEmbedBridge` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `JWStringMultiline` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `SaveImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
