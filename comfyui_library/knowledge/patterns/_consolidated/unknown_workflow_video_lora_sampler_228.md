---
name: unknown_workflow_video_lora_sampler_228
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8393
common_nodes: [CreateCFGScheduleFloatList, INTConstant, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/04-01-02-WAN2.2-文生视频-kijai_1990967408930267138.json, 视频生成/文生视频/CG迷-Wan2.2 Kijai文生视频工作流（支持gguf）_1950485785722146818.json, 视频生成/文生视频/KJ流+官方新版LightX2V文生视频_1952405030194360321.json, 视频生成/文生视频/Wan2.2 Dyno文生视频加速版V2(KJ版)_1974801904645574658.json, 视频生成/文生视频/Wan2.2 Smooth Mix高动态文生视频V2（KJ版）_1979020058171183105.json, 视频生成/文生视频/文生视频（Wan2.2）高质量加速版_1952329679653023745.json, 视频生成/文生视频/最新WAN2.2 KJ版 T2V 文生视频加速版工作流_1977042886363631618.json, 视频生成/文生视频/最新万相wan2.2-14B文生视频KJ极速版，效果炸裂_1950109522175115265.json, 视频生成/文生视频/（4+4步高质量高速度）Wan2.2 Smooth Mix高动态差异模型文生视频V1（KJ版）_1978818783190093825.json, 视频生成/文生视频/（4+4步）Wan2.2 HoloCine电影多镜头文生视频（KJ版-目前效果不佳）_1982404928775831554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_228

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/04-01-02-WAN2.2-文生视频-kijai_1990967408930267138.json、视频生成/文生视频/CG迷-Wan2.2 Kijai文生视频工作流（支持gguf）_1950485785722146818.json、视频生成/文生视频/KJ流+官方新版LightX2V文生视频_1952405030194360321.json、视频生成/文生视频/Wan2.2 Dyno文生视频加速版V2(KJ版)_1974801904645574658.json、视频生成/文生视频/Wan2.2 Smooth Mix高动态文生视频V2（KJ版）_1979020058171183105.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 9/10 个有
- `CR Prompt Text` —— 8/10 个有
- `GetImageSizeAndCount` —— 8/10 个有
- `JWInteger` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `ImageFromBatch+` —— 4/10 个有
- `GetNode` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `WanVideoEasyCache` —— 2/10 个有
- `JjkText` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `TT_img_enc` —— 1/10 个有
- `WanVideoContextOptions` —— 1/10 个有
- `WanVideoLoraSelectMulti` —— 1/10 个有
- `easy seed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
