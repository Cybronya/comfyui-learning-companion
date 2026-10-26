---
name: unknown_workflow_video_lora_sampler_36
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.95824
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, INTConstant, ImageResize+, JWInteger, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/12shouweizhengao_2048982440785485825.json, 图片生成/反推提示词/45shouweizhenliuchang_2050102530000076802.json, 图片生成/图生图/Wan2.2首尾帧KJ8步_1952288273785933825.json, 图片生成/图生图/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1995029039742115842.json, 图片生成/文生图/首尾帧视频-WAN2.2高质量版_1980937502708158465.json, 视频生成/图生视频/WAN2.2-首尾帧视频工作流_1981935370910744577.json, 视频生成/图生视频/WAN2.2毛茸茸首尾帧动画_1978297110992969730.json, 视频生成/图生视频/WAN2.2首尾帧视频工作流_1992060788846252034.json, 视频生成/图生视频/WAN2.2首尾帧高清快速出视频-高级版_1963555388825358337.json, 视频生成/图生视频/WAN2.2首尾帧高质量版_2027622896310427649.json, 视频生成/图生视频/WAN2.2高质量首尾帧视频加速版（3分钟版）_1981195312264110081.json, 视频生成/图生视频/Wan2.2 首尾帧视频工作流_1992174428303806466.json, 视频生成/图生视频/Wan2.2_KJ版 首尾帧+补帧_2019656861171060738.json, 视频生成/图生视频/Wan2.2_KJ版 首尾帧视频+补帧_高质量加速版V2_1998010318326497281.json, 视频生成/图生视频/Wan2.2_KJ版+首尾帧生视频+补帧_高质量加速版_2000475113990520833.json, 视频生成/图生视频/Wan2.2_KJ版+首尾帧生视频-阿浩_2026893415455133697.json, 视频生成/图生视频/Wan2.2首尾帧视频+补帧_KJ版_2018932205057216513.json, 视频生成/图生视频/Wan2.6高质量补帧首尾帧视频puls_2018481658378330113.json, 视频生成/图生视频/图生视频首尾帧快速版-WAN2.2稳定版_2025740661340774402.json, 视频生成/图生视频/课件25：WAN2.2首尾帧视频工作流（开源）_2103640919990951938.json, 视频生成/图生视频/首尾帧WAN2.2-AIGC大赏_2063448324002373634.json, 视频生成/图生视频/首尾帧生视频加速-WAN2.2配LoRA权重高质量版_2037500087261208578.json, 视频生成/图生视频/首尾帧视频 - WAN2.2_KJ_高质量加速版_1971037021902905346.json, 视频生成/图生视频/首尾帧视频 - WAN2.2_KJ_高质量加速画质修复版_1976556715808264194.json, 视频生成/图生视频/首尾帧视频 - WAN2.2_KJ_高质量加速画质修复版_2041413117292318723.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/反推提示词/12shouweizhengao_2048982440785485825.json、图片生成/反推提示词/45shouweizhenliuchang_2050102530000076802.json、图片生成/图生图/Wan2.2首尾帧KJ8步_1952288273785933825.json、图片生成/图生图/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1995029039742115842.json、图片生成/文生图/首尾帧视频-WAN2.2高质量版_1980937502708158465.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 25 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageResize+`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 24/25 个有
- `SimpleMath+` —— 23/25 个有
- `ColorMatch` —— 9/25 个有
- `WanVideoSLG` —— 9/25 个有
- `Float` —— 8/25 个有
- `DF_Int_to_Float` —— 6/25 个有
- `RIFE VFI` —— 6/25 个有
- `MuyeTextEditOutput` —— 2/25 个有
- `RTXVideoSuperResolution` —— 2/25 个有
- `GetNode` —— 1/25 个有
- `Int` —— 1/25 个有
- `Label (rgthree)` —— 1/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/25 个有
- `SaveImage` —— 1/25 个有
- `SetNode` —— 1/25 个有
- `TT_img_enc_v2` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
