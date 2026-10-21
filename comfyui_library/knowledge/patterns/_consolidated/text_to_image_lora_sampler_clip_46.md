---
name: text_to_image_lora_sampler_clip_46
type: Text To Image
frequency: 16
level: strong
coverage: 0.728875
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/图像编辑文生图图生图｜MIniMax-H3图片编辑工作流_2088336424029474818.json, 视频生成/图生视频/Minimax-H3lora)ENG8步多参生视频(双时钟图生极速2分钟出5秒ENG_2087129153064751106.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜SLA脸部动作稳定版_2097906883771330562.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意生成_2094540734518091777.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意视频制作_2107673663351910401.json, 视频生成/图生视频/Minimax-H3电商宣传广告｜产品视频高质量生成_2095594718758531074.json, 视频生成/图生视频/动态最强参考生视频｜MiniMax H3 V1版图生视频_2095050766850551809.json, 视频生成/图生视频/文戏短剧专用工作流｜MINIMAX-H3 图生视频细腻演绎_2096245265643692034.json, 视频生成/图生视频/电影感Eros Beta4｜Minimax H3加速Upscaler参考生视频_2094921602256424961.json, 视频生成/文生视频/9月30日目前最强武戏高动态 极速高清自动提示词加手动提示词2选1_2105345913706340354.json, 视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强_2099911788254027778.json, 视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强宫格图生视频_2099910070346801153.json, 视频生成/文生视频/H3双采全能工作流V2 音频驱动数字人参考生视频_2099905442196574210.json, 视频生成/文生视频/H3双采全能工作流V2文戏不油武戏动态强宫格图生视频_2100639256866811906.json, 视频生成/文生视频/MiniMax H3高动文武双修工作流，文生视频视频生视频图生视频方案_2107167458216996865.json, 视频生成/文生视频/minimaxh3高动文武双修工作流 视频生成均衡方案_2108674482876534786.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/图像编辑文生图图生图｜MIniMax-H3图片编辑工作流_2088336424029474818.json、视频生成/图生视频/Minimax-H3lora)ENG8步多参生视频(双时钟图生极速2分钟出5秒ENG_2087129153064751106.json、视频生成/图生视频/Minimax-H3开源参考生视频｜SLA脸部动作稳定版_2097906883771330562.json、视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意生成_2094540734518091777.json、视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意视频制作_2107673663351910401.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 15/16 个有
- `LoraLoaderBypassModelOnly` —— 15/16 个有
- `MiniMaxH3AVDecodeT8` —— 15/16 个有
- `MiniMaxH3AudioConditioningT8` —— 15/16 个有
- `PrimitiveFloat` —— 15/16 个有
- `VHS_VideoCombine` —— 15/16 个有
- `ModelAttentionBackend` —— 14/16 个有
- `SolAttnMiniMax` —— 13/16 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 11/16 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 11/16 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 11/16 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 11/16 个有
- `GetNode` —— 10/16 个有
- `SetNode` —— 10/16 个有
- `Fast Groups Bypasser (rgthree)` —— 8/16 个有
- `Float` —— 8/16 个有
- `SaveImage` —— 8/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/16 个有
- `PreviewImage` —— 5/16 个有
- `PreviewAny` —— 4/16 个有
- `ConcatTextOfUtils` —— 3/16 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 3/16 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 3/16 个有
- `RH_LLMAPI_Pro_Node` —— 3/16 个有
- `LoadAudio` —— 2/16 个有
- `VAEDecodeAudio` —— 2/16 个有
- `ImageConcanate` —— 1/16 个有
- `ImpactSwitch` —— 1/16 个有
- `MiniMaxH3StillConditioningT8` —— 1/16 个有
- `MiniMaxH3StillDecodeT8` —— 1/16 个有
- `MiniMaxH3StillPreflightT8` —— 1/16 个有
- `Text Multiline` —— 1/16 个有
- `easy cleanGpuUsed` —— 1/16 个有
- `忽略多组孤海` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
