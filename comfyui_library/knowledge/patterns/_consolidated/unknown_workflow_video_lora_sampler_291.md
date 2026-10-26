---
name: unknown_workflow_video_lora_sampler_291
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.883
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, ImageToMask, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddTTMLatents, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(手动工具版)TTM路径编辑图生视频V1_1990441820280807425.json, 视频生成/图生视频/TTM-视频主体轨迹移动控制_1991157733022085121.json, 视频生成/图生视频/TTM任意编辑视频生成-Aiwood_1990244516261228546.json, 视频生成/图生视频/TTM编辑轨迹动作引导生成视频_1990327033626587137.json, 视频生成/图生视频/Time-to-Move框架：关键帧引导生成AI视频，精确控制视频元素移动！_1990969622830718977.json, 视频生成/图生视频/Wan2_2_I2V_TimeToMove 运动控制图生视频_1991333399692685313.json, 视频生成/图生视频/wanvideo2_2_I2V_A14B_TimeToMove_example_1990459550644002818.json, 视频生成/图生视频/精确版 TTM-视频主体轨迹移动控制_1999381454922579970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_291

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/(手动工具版)TTM路径编辑图生视频V1_1990441820280807425.json、视频生成/图生视频/TTM-视频主体轨迹移动控制_1991157733022085121.json、视频生成/图生视频/TTM任意编辑视频生成-Aiwood_1990244516261228546.json、视频生成/图生视频/TTM编辑轨迹动作引导生成视频_1990327033626587137.json、视频生成/图生视频/Time-to-Move框架：关键帧引导生成AI视频，精确控制视频元素移动！_1990969622830718977.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageToMask`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddTTMLatents`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `CLIPLoader` —— 1/8 个有
- `CLIPTextEncode` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `VHS_SelectImages` —— 1/8 个有
- `WanVideoImageToVideoEncode_v2` —— 1/8 个有
- `WanVideoTextEmbedBridge` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
