---
name: text_to_image_lora_sampler_clip_189
type: Text To Image
frequency: 10
level: strong
coverage: 0.9198
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MINIMAX H3多参生视频，文生视频图生视频双模式_2110819887017975810.json, 视频生成/图生视频/MiniMax H3图片参考生成带货视频 加速版电商内容制作_2098699036625821698.json, 视频生成/图生视频/MiniMax H3多参图像音频生视频｜Singulari极速加速版_2107645905364152321.json, 视频生成/图生视频/MiniMax H3多图加音频参考，极速生视频优化方案_2111205029150547969.json, 视频生成/图生视频/MiniMax H3多图参考优化版｜音频参考极速生视频_2106612379277680642.json, 视频生成/图生视频/MiniMax H3多图参考音频参考加速优化版，图生视频高效产出工具_2105720092976836609.json, 视频生成/图生视频/MiniMax H3极速生视频优化版｜多图加音频参考全支持_2111086493161836545.json, 视频生成/图生视频/MiniMax_H3角色替换工作流，文生视频视频生视频图生视频处理方案_2109459137858985985.json, 视频生成/文生视频/H3多图参考音频参考极速生视频优化版 多模态创作_2099928699171860482.json, 视频生成/文生视频/MiniMax H3角色替换工作流，文生视频视频生视频图生视频处理方案_2107202145123659778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_189

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MINIMAX H3多参生视频，文生视频图生视频双模式_2110819887017975810.json、视频生成/图生视频/MiniMax H3图片参考生成带货视频 加速版电商内容制作_2098699036625821698.json、视频生成/图生视频/MiniMax H3多参图像音频生视频｜Singulari极速加速版_2107645905364152321.json、视频生成/图生视频/MiniMax H3多图加音频参考，极速生视频优化方案_2111205029150547969.json、视频生成/图生视频/MiniMax H3多图参考优化版｜音频参考极速生视频_2106612379277680642.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/10 个有
- `PathchSageAttentionKJ` —— 9/10 个有
- `EasyCache` —— 8/10 个有
- `ShowAnything|Mie` —— 8/10 个有
- `CR Prompt Text` —— 7/10 个有
- `ImageResizeKJv2` —— 7/10 个有
- `Int` —— 7/10 个有
- `LoadAudio` —— 7/10 个有
- `SaveImage` —— 7/10 个有
- `intToFloat _O` —— 7/10 个有
- `ImageFromBatch` —— 3/10 个有
- `PreviewAny` —— 3/10 个有
- `ResolutionSelector` —— 3/10 个有
- `GetVideoComponents` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `Text Multiline` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `llama_cpp_instruct_adv` —— 2/10 个有
- `llama_cpp_model_loader` —— 2/10 个有
- `llama_cpp_parameters` —— 2/10 个有
- `ImpactSwitch` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `RH_Astra` —— 1/10 个有
- `VHS_VideoCombine` —— 1/10 个有
- `easy float` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
