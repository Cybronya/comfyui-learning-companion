---
name: unknown_workflow_sampler_clip_unet_171
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.955875
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CreateVideo, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/DasiwaV10首尾帧生视频_2036098308422242306.json, 视频生成/图生视频/DasiwaV10首帧生视频_2036097978263412738.json, 视频生成/图生视频/SwoothMix首帧生视频_2031653989615411202.json, 视频生成/图生视频/WAN2.2 视频生成（首尾帧，首帧）_2019023279008260098.json, 视频生成/图生视频/remix_v3.0首尾帧生视频_2036071693340385282.json, 视频生成/图生视频/remix_v3.0首帧生视频_2036017252914434050.json, 视频生成/图生视频/wan2.2_SmoothMix首尾帧生视频_2031673957350379522.json, 视频生成/图生视频/wan2.2首帧生视频4steps加速工作流_2030866059493904385.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_171

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/DasiwaV10首尾帧生视频_2036098308422242306.json、视频生成/图生视频/DasiwaV10首帧生视频_2036097978263412738.json、视频生成/图生视频/SwoothMix首帧生视频_2031653989615411202.json、视频生成/图生视频/WAN2.2 视频生成（首尾帧，首帧）_2019023279008260098.json、视频生成/图生视频/remix_v3.0首尾帧生视频_2036071693340385282.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 7/8 个有
- `LayerUtility: PurgeVRAM V2` —— 7/8 个有
- `SimpleMath+` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `FloatConstant` —— 6/8 个有
- `INTConstant` —— 6/8 个有
- `ModelPatchTorchSettings` —— 6/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `WanImageToVideo` —— 5/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `WanFirstLastFrameToVideo` —— 4/8 个有
- `Int` —— 2/8 个有
- `ApplySageAttention` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 88% |
| Prompt 约束强度(CFG) | 4 | 4 - 14 | 8 | 37% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler_ancestral | - | 8 | 75% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 14，8 个样本，取值分散，一致性仅 37%
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，8 个样本，一致性 75%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
