---
name: unknown_workflow_video_sampler_clip_17
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.87319
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Bernini 角色替换_2069319914443333634.json, 视频生成/图生视频/Smooth+FMLF 首尾多帧视频_1988615220765614082.json, 视频生成/图生视频/SmoothMix-V2.0首中尾多帧视频生成+补帧+放大_2021154094072733697.json, 视频生成/图生视频/SmoothMix-V2.0首中尾多帧视频生成+补帧+放大_2041753432205299714.json, 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2010685472720293889.json, 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2022695348518522881.json, 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2059832130892550145.json, 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2063803655928766465.json, 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2069687401794064385.json, 视频生成/图生视频/Wan2.2_Remix（首中尾帧)_2001639345427738626.json, 视频生成/图生视频/Wan2.2_Remix（首尾帧)_2001276328982740993.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2053500201926705153.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2054607136101027841.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063711056727461890.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063712287315292162.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063714093613281281.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063914082952114178.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2072973666828251138.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2083074284628566017.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2048315037026099202.json, 视频生成/图生视频/首尾帧视频-rh-WAN2.2-RemixV2-I2V-模板_2022797713682735106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/Bernini 角色替换_2069319914443333634.json、视频生成/图生视频/Smooth+FMLF 首尾多帧视频_1988615220765614082.json、视频生成/图生视频/SmoothMix-V2.0首中尾多帧视频生成+补帧+放大_2021154094072733697.json、视频生成/图生视频/SmoothMix-V2.0首中尾多帧视频生成+补帧+放大_2041753432205299714.json、视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2010685472720293889.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 20/21 个有
- `LoadImage` —— 20/21 个有
- `ModelSamplingSD3` —— 20/21 个有
- `LoraLoaderModelOnly` —— 19/21 个有
- `ModelPatchTorchSettings` —— 19/21 个有
- `SimpleMath+` —— 18/21 个有
- `WanFirstMiddleLastFrameToVideo` —— 18/21 个有
- `GetNode` —— 12/21 个有
- `SetNode` —— 12/21 个有
- `RIFE VFI` —— 5/21 个有
- `easy cleanGpuUsed` —— 5/21 个有
- `Int` —— 3/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/21 个有
- `PreviewImage` —— 3/21 个有
- `ImageScaleBy` —— 2/21 个有
- `WanFirstLastFrameToVideo` —— 2/21 个有
- `BerniniConditioning` —— 1/21 个有
- `Fast Groups Bypasser (rgthree)` —— 1/21 个有
- `ImageLoader` —— 1/21 个有
- `MathExpression|pysssss` —— 1/21 个有
- `VHS_LoadVideo` —— 1/21 个有
- `VHS_VideoInfoLoaded` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 21 | 95% |
| Prompt 约束强度(CFG) | 6 | 4 - 20 | 21 | 42% |
| 采样算法 | 1 | 1 - 1 | 21 | 100% |
| 调度器 | euler | - | 21 | 95% |
| 重绘幅度 | beta | - | 21 | 48% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，21 个样本，一致性 95%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 20，21 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，21 个样本，一致性 95%
- 重绘幅度 最常用 beta，21 个样本，一致性 48%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
