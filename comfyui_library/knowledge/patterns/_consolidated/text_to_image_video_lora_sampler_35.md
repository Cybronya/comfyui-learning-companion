---
name: text_to_image_video_lora_sampler_35
type: Text To Image
frequency: 18
level: strong
coverage: 0.930556
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, EnhancedLoadDiffusionModel, Int, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3 bf16-lightx2v Flashvsr高清画质图生图处理工具_2101772141397102594.json, 视频生成/图生视频/FL2AV bf16 lightx2v 8步加速v2｜MInimaxH3图生视频正式版_2091242587490447362.json, 视频生成/图生视频/Flashvsr高清画质图生视频｜MInimaxH3_i2AV_bf16-lightx2v_1.0_2095801670214180865.json, 视频生成/图生视频/Flashvsr高清画质｜MInimaxH3 i2AV bf16-lightx2v图生视频_2091757024878092289.json, 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版｜8步加速出片更快_2099513847114719233.json, 视频生成/图生视频/MiniMax H3 FL2AV BF16 LightX2V 1.0正式版8步加速V2，图生视频方案_2106843322143830017.json, 视频生成/图生视频/MiniMax_H3_FL2AV_BF16_LightX2V_1.0正式版8步加速V2，图生视频方案_2110532111202603010.json, 视频生成/图生视频/MinimaxH3 i2AV高清画质｜bf16+lightx2v Flashvsr加持_2099912857197572097.json, 视频生成/图生视频/MinimaxH3八步加速极速版T2｜文生视频秒级出片_2097188584955666433.json, 视频生成/图生视频/lightx2v_1.0 Flashvsr高清画质i2AV｜MInimaxH3图生视频工作流_2088137110292353025.json, 视频生成/图生视频/lightx2v_1.0正式版8步加速i2AV｜MInimaxH3图生视频工作流_2088174200824623105.json, 视频生成/图生视频/八步加速极速出片｜MinimaxH3文生视频T2版本_2101128554191867906.json, 视频生成/图生视频/八步加速极速版T1｜MinimaxH3 图生视频_2089307044976349186.json, 视频生成/图生视频/八步加速极速版T1｜MinimaxH3 图生视频_2090724301610766338.json, 视频生成/图生视频/八步加速极速版T1｜MinimaxH3图生视频生成_2090920040836190210.json, 视频生成/图生视频/八步加速极速版T2｜MinimaxH3 图生视频_2089293730955223041.json, 视频生成/图生视频/八步加速极速版T2｜MinimaxH3图生视频生成_2093751589004726274.json, 视频生成/图生视频/正式版8步加速v2图生视频｜MInimaxH3_FL2AV_bf16-lightx2v_1.0_2095547323186241538.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/MiniMax H3 bf16-lightx2v Flashvsr高清画质图生图处理工具_2101772141397102594.json、视频生成/图生视频/FL2AV bf16 lightx2v 8步加速v2｜MInimaxH3图生视频正式版_2091242587490447362.json、视频生成/图生视频/Flashvsr高清画质图生视频｜MInimaxH3_i2AV_bf16-lightx2v_1.0_2095801670214180865.json、视频生成/图生视频/Flashvsr高清画质｜MInimaxH3 i2AV bf16-lightx2v图生视频_2091757024878092289.json、视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版｜8步加速出片更快_2099513847114719233.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 16/18 个有
- `DF_Get_image_size` —— 9/18 个有
- `FlashVSR_SM_KSampler` —— 9/18 个有
- `FlashVSR_SM_Model` —— 9/18 个有
- `GetImageRangeFromBatch` —— 9/18 个有
- `JWInteger` —— 9/18 个有
- `LayerUtility: PurgeVRAM V2` —— 9/18 个有
- `CreateVideo` —— 5/18 个有
- `SaveVideo` —— 5/18 个有
- `SaveImage` —— 3/18 个有
- `EmptyImage` —— 2/18 个有
- `PreviewImage` —— 2/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（19/18 个样本）：Steps较低可能导致细节不足
