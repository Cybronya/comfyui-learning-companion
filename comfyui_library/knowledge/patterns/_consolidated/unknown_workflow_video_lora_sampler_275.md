---
name: unknown_workflow_video_lora_sampler_275
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.666875
common_nodes: [LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, PreviewImage, SetNode, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Lynx高保真IP迁移工作流升级版_2073214069175312386.json, 图片生成/图生图/人物图片代替视频lora模型--Lynx免训练ID_1976962835324522498.json, 视频生成/图生视频/无限画布工作流-嘉宾视频_1977229583860801538.json, 视频生成/文生视频/Lynx免训练ID一致性文生视频Full版V2_1975438784533762049.json, 视频生成/文生视频/Lynx免训练ID一致性文生视频Lite版V2(横版)_1975435330138542082.json, 视频生成/文生视频/Lynx免训练ID一致性文生视频Lite版V2(竖版)_1975446783209902081.json, 视频生成/文生视频/Wan2.1_T2V_Lynx人物一致性文生视频_1976584449313869825.json, 视频生成/文生视频/Wanvideo-lynx超级人物一致性文生视频_1976840032592052226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_275

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Lynx高保真IP迁移工作流升级版_2073214069175312386.json、图片生成/图生图/人物图片代替视频lora模型--Lynx免训练ID_1976962835324522498.json、视频生成/图生视频/无限画布工作流-嘉宾视频_1977229583860801538.json、视频生成/文生视频/Lynx免训练ID一致性文生视频Full版V2_1975438784533762049.json、视频生成/文生视频/Lynx免训练ID一致性文生视频Lite版V2(横版)_1975435330138542082.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 8 个 workflow 都包含：
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/8 个有
- `ImageConcatMulti` —— 5/8 个有
- `ImageFromBatch+` —— 5/8 个有
- `CR Prompt Text` —— 4/8 个有
- `GetImageSizeAndCount` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `CR Text` —— 3/8 个有
- `AdvancedImageSelector` —— 1/8 个有
- `FancyTimerNode` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `RMBG` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
