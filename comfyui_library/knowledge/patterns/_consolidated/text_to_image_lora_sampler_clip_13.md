---
name: text_to_image_lora_sampler_clip_13
type: Text To Image
frequency: 30
level: strong
coverage: 0.928033
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EasyCache, EmptyLatentImage, Int, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax_H3角色替换工作流，文生视频视频生视频图生视频处理方案_2109459137858985985.json, 视频生成/图生视频/REF2V图生视频生成｜地表最强开源Minimax H3运镜_2096664623201218561.json, 视频生成/图生视频/地表最强开源 Minimax H3 REF2V｜角色一致性图生视频运镜_2096852990467592194.json, 视频生成/文生视频/H3多图参考音频参考极速生视频优化版 多模态创作_2099928699171860482.json, 视频生成/文生视频/MiniMax H3多图+音频参考极速生视频优化版｜出片快人一步_2108028586644041729.json, 视频生成/文生视频/MiniMax H3多图加音频参考｜加速优化出片更快_2097164515363352577.json, 视频生成/文生视频/MiniMax H3多图加音频参考｜生视频加速版效率翻倍_2107653791804903426.json, 视频生成/文生视频/MiniMax H3多图参考音频参考加速优化版工作流，文生视频图生视频方案_2107895013450534914.json, 视频生成/文生视频/MiniMax H3多图参考音频参考加速版工作流，文生视频图生视频处理方案_2107893442566254594.json, 视频生成/文生视频/MiniMax H3多图参考音频参考极速生视频优化版 多模态输入_2105361187130142721.json, 视频生成/文生视频/MiniMax H3多图参考音频参考极速生视频优化版工作流，文生视频图生视频方案_2108272979615510530.json, 视频生成/文生视频/MiniMax H3多图参考音频参考极速生视频优化版，文生视频图生视频_2106826270205108225.json, 视频生成/文生视频/MiniMax H3多图参考音频参考｜加速优化版生成_2094524838961565698.json, 视频生成/文生视频/MiniMax H3多图音频参考极速生视频 优化版多模态创作_2098652804280832001.json, 视频生成/文生视频/MiniMax H3多图音频双参考｜加速优化版视频更稳定_2107655293843890177.json, 视频生成/文生视频/MiniMax H3极速生视频优化版｜多图参考加音频参考双加持_2105120322000347138.json, 视频生成/文生视频/MiniMax H3角色替换工作流，文生视频视频生视频图生视频处理方案_2107202145123659778.json, 视频生成/文生视频/多图+音频参考加速｜MiniMax H3优化版生视频_2094745022984974337.json, 视频生成/文生视频/多图加音频双参考输入 MiniMax H3极速生视频优化版_2104268127499542529.json, 视频生成/文生视频/多图参考加音频参考｜MiniMax H3 加速优化版 参考生视频更听话_2105490121989648386.json, 视频生成/文生视频/多图参考音频参考加速优化版｜MiniMax H3文生视频生成_2097027445839978498.json, 视频生成/文生视频/多图参考音频参考加速优化｜MiniMax H3文生图生视频_2091270580233400322.json, 视频生成/文生视频/多图参考音频参考加速版｜MiniMax H3图生视频生成_2097046537246433282.json, 视频生成/文生视频/多图参考音频参考加速版｜MiniMax H3文生视频_2092342768986320898.json, 视频生成/文生视频/多图参考音频参考极速生视频｜MiniMax H3优化版_2092070354985508866.json, 视频生成/文生视频/多图参考音频参考｜MiniMax H3加速版图生视频_2090895313207910402.json, 视频生成/文生视频/多图参考音频参考｜MiniMax H3极速生视频优化版_2090662418232991745.json, 视频生成/文生视频/多图音频参考加速版｜MiniMax H3图生视频_2091193733667704834.json, 视频生成/文生视频/极速生视频优化版｜MiniMax H3多图音频参考生成_2094750958134841346.json, 视频生成/文生视频/音频参考极速生视频｜MiniMax H3多图参考优化版_2090836383433842690.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3角色替换工作流，文生视频视频生视频图生视频处理方案_2109459137858985985.json、视频生成/图生视频/REF2V图生视频生成｜地表最强开源Minimax H3运镜_2096664623201218561.json、视频生成/图生视频/地表最强开源 Minimax H3 REF2V｜角色一致性图生视频运镜_2096852990467592194.json、视频生成/文生视频/H3多图参考音频参考极速生视频优化版 多模态创作_2099928699171860482.json、视频生成/文生视频/MiniMax H3多图+音频参考极速生视频优化版｜出片快人一步_2108028586644041729.json…）

- **类型**：Text To Image
- **样本数**：30
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 30 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `EmptyLatentImage`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
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
- `ImageResizeKJv2` —— 28/30 个有
- `ShowAnything|Mie` —— 28/30 个有
- `intToFloat _O` —— 27/30 个有
- `LoadAudio` —— 26/30 个有
- `CR Prompt Text` —— 20/30 个有
- `SaveImage` —— 15/30 个有
- `PrimitiveStringMultiline` —— 8/30 个有
- `ImageFromBatch` —— 2/30 个有
- `ImpactSwitch` —— 2/30 个有
- `PreviewAny` —— 2/30 个有
- `PreviewImage` —— 2/30 个有
- `ResolutionSelector` —— 2/30 个有
- `Text Multiline` —— 2/30 个有
- `TextBox` —— 2/30 个有
- `VHS_LoadVideo` —— 2/30 个有
- `easy showAnything` —— 2/30 个有
- `llama_cpp_instruct_adv` —— 2/30 个有
- `llama_cpp_model_loader` —— 2/30 个有
- `llama_cpp_parameters` —— 2/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 30 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 30 | 100% |
| 采样算法 | er_sde | - | 30 | 100% |
| 调度器 | beta | - | 30 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 30 | 100% |
| 宽度 | 80 | 80 - 80 | 30 | 100% |
| 高度 | 80 | 80 - 80 | 30 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/30 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，30 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，30 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，30 个样本，一致性 100%
- 调度器 最常用 beta，30 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，30 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，30 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，30 个样本，取值集中（一致性 100%）
- 高发问题（30/30 个样本）：Steps较低可能导致细节不足
