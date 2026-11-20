---
name: text_to_image_video_lora_sampler_49
type: Text To Image
frequency: 15
level: strong
coverage: 0.792267
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 I2V图生视频｜Fused ACC八步极速出片_2097147575894888449.json, 视频生成/图生视频/MiniMax H3 Ref2AV bf16 lightx2v八步加速V2工作流，图生视频方案_2106095744552886273.json, 视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词T6工作流，角色一致性图生视频_2106097208906043393.json, 视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词，角色表演图生视频工作流_2103588976929099778.json, 视频生成/图生视频/MiniMax H3全参连续帧提示词自动优化工作流，图生视频高效创作方案_2106094286554099714.json, 视频生成/图生视频/Ref2AV八步加速V2｜MInimaxH3 bf16-lightx2v图生视频_2094721166920478721.json, 视频生成/图生视频/T2V文生视频加速流AITUDOU MiniMax H3图生视频工作流_2088399160956510209.json, 视频生成/图生视频/T2V文生视频加速流｜AITUDOU-MiniMax H3图生视频工作流_2088378615552634882.json, 视频生成/图生视频/T6全参官方指南｜minimaxh3自动扩展提示词分镜出图_2094333256052334594.json, 视频生成/图生视频/T8全参官方指南｜minimaxh3扩展提示词角色一致性生视频_2094463893199482882.json, 视频生成/图生视频/lightx2v 8step加速｜MiniMax H3图生视频快速出片_2088748531585736705.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词_2086537843907846146.json, 视频生成/图生视频/全参连续帧优化｜minimaxh3提示词自动图生视频生成_2094719853226717186.json, 视频生成/图生视频/全能参考数字人｜AITUDOU MiniMax H3 人物音频一致性_2089296635812737025.json, 视频生成/图生视频/古装美女扮相图生视频｜古风人像一键动起来_2098703419811909633.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_49

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 I2V图生视频｜Fused ACC八步极速出片_2097147575894888449.json、视频生成/图生视频/MiniMax H3 Ref2AV bf16 lightx2v八步加速V2工作流，图生视频方案_2106095744552886273.json、视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词T6工作流，角色一致性图生视频_2106097208906043393.json、视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词，角色表演图生视频工作流_2103588976929099778.json、视频生成/图生视频/MiniMax H3全参连续帧提示词自动优化工作流，图生视频高效创作方案_2106094286554099714.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 13/15 个有
- `LoadImage` —— 13/15 个有
- `PrimitiveFloat` —— 11/15 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 9/15 个有
- `RHHiddenNodes` —— 8/15 个有
- `ImageConcatenateMulti_UTK` —— 7/15 个有
- `PreviewImage` —— 7/15 个有
- `GetNode` —— 5/15 个有
- `SetNode` —— 5/15 个有
- `LoadAudio` —— 4/15 个有
- `MiniMaxH3ImageToVideo` —— 4/15 个有
- `SaveImage` —— 4/15 个有
- `easy showAnything` —— 4/15 个有
- `EnhancedLoadDiffusionModel` —— 3/15 个有
- `LoraLoaderBypassModelOnly` —— 3/15 个有
- `Float` —— 2/15 个有
- `MiniMaxH3ReferenceToVideo` —— 2/15 个有
- `RH_Captioner` —— 2/15 个有
- `SigmasGraph` —— 2/15 个有
- `TextConcatenate_UTK` —— 2/15 个有
- `easy imageSplitGrid` —— 2/15 个有
- `easy indexAnything` —— 2/15 个有
- `Label (rgthree)` —— 1/15 个有
- `PreviewAny` —— 1/15 个有
- `RH_LLMAPI_Pro_Node` —— 1/15 个有
- `ZNGB_AudioCrop` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
