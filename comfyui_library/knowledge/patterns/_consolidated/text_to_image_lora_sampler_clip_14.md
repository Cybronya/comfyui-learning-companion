---
name: text_to_image_lora_sampler_clip_14
type: Text To Image
frequency: 27
level: strong
coverage: 0.893111
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [ShowAnything|Mie, intToFloat _O, CR Prompt Text]
members: [视频生成/图生视频/MiniMax H3多图加音频参考，极速生视频优化方案_2111205029150547969.json, 视频生成/图生视频/MiniMax H3多图参考优化版_音频参考极速生视频_2106612379277680642.json, 视频生成/图生视频/MiniMax H3多图参考生成视频图生视频与视频生视频全能参考方案_2107257293007052802.json, 视频生成/图生视频/MiniMax H3多图参考生成视频，图生视频与视频生视频全能参考方案_2102813018273968130.json, 视频生成/图生视频/MiniMax H3多图参考生视频图生视频处理生成工具_2101745060818808833.json, 视频生成/图生视频/MiniMax H3多图参考生视频工作流_视频生视频图生视频多素材融合方案_2105760424162586626.json, 视频生成/图生视频/MiniMax H3多图参考生视频｜几张图一起喂｜人物场景一致性拉满_2102579245317967874.json, 视频生成/图生视频/MiniMax H3多图参考生视频｜多素材参考一致性视频生成_2108015949080260609.json, 视频生成/图生视频/MiniMax H3多图参考音频参考加速优化版_图生视频高效产出工具_2105720092976836609.json, 视频生成/图生视频/MiniMax H3开源加速多宫格稳定出片｜海螺多参漫剧短剧人物特效角色设计图生视频_2089710412790067202.json, 视频生成/图生视频/MiniMax H3开源加速版｜海螺多参多宫格稳定出片｜漫剧短剧加速搞定_2102600651598553090.json, 视频生成/图生视频/MiniMax H3极速生视频优化版｜多图加音频参考全支持_2111086493161836545.json, 视频生成/图生视频/MiniMax H3首尾帧加速版_图生视频运镜更流畅_2106610629435019266.json, 视频生成/图生视频/MiniMax H3首尾帧加速版｜图生视频出片更快更稳_2111084749388341249.json, 视频生成/图生视频/MiniMax H3首尾帧视频加速版，图生视频更流畅_2111203485525037057.json, 视频生成/图生视频/MiniMax h3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版_2085308700373381121.json, 视频生成/图生视频/MiniMax+H3加速版图文一键生视频｜运镜丝滑出片快_2111327354969747458.json, 视频生成/图生视频/MiniMax_H3 I2V加速多参考生视频，高效图生视频工具_2110532068039028738.json, 视频生成/图生视频/MiniMax_H3_I2V加速多参考生视频，高效图生视频工具_2111269686322225154.json, 视频生成/图生视频/MiniMax_H3_I2V加速多参考视频生成工作流，图生视频高效创作工具_2109863281748963329.json, 视频生成/图生视频/MiniMax_H3_I2V加速首尾帧工作流，图生视频高效创作工具_2110535989906202626.json, 视频生成/图生视频/MiniMax_H3多图参考生成视频_图生视频与视频生视频全能参考方案_2106558188098248705.json, 视频生成/图生视频/MiniMax_H3多图参考生成视频图生视频与视频生视频全能参考方案_2109448439166750721.json, 视频生成/图生视频/MiniMax_H3多图参考生成视频，图生视频与视频生视频全能参考方案_2106558188098248705.json, 视频生成/图生视频/MiniMax_H3角色替换工作流，文生视频视频生视频图生视频处理方案_2109459137858985985.json, 视频生成/图生视频/加速版MiniMax_H3图文直出视频｜一句话配一张图，成片一键拿_2099445108864282625.json, 视频生成/文生视频/MiniMax H3角色替换工作流，文生视频视频生视频图生视频处理方案_2107202145123659778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多图加音频参考，极速生视频优化方案_2111205029150547969.json、视频生成/图生视频/MiniMax H3多图参考优化版_音频参考极速生视频_2106612379277680642.json、视频生成/图生视频/MiniMax H3多图参考生成视频图生视频与视频生视频全能参考方案_2107257293007052802.json、视频生成/图生视频/MiniMax H3多图参考生成视频，图生视频与视频生视频全能参考方案_2102813018273968130.json、视频生成/图生视频/MiniMax H3多图参考生视频图生视频处理生成工具_2101745060818808833.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 21/27 个有
- `MiniMaxH3ReferenceToVideo` —— 18/27 个有
- `PrimitiveFloat` —— 18/27 个有
- `ResolutionSelector` —— 18/27 个有
- `PrimitiveStringMultiline` —— 17/27 个有
- `SaveImage` —— 16/27 个有
- `EasyCache` —— 14/27 个有
- `PathchSageAttentionKJ` —— 14/27 个有
- `LoadAudio` —— 13/27 个有
- `PreviewImage` —— 11/27 个有
- `ShowAnything|Mie` —— 11/27 个有
- `CR Prompt Text` —— 10/27 个有
- `EmptyImage` —— 9/27 个有
- `ImageResizeKJv2` —— 9/27 个有
- `Int` —— 9/27 个有
- `MiniMaxH3ImageToVideo` —— 9/27 个有
- `intToFloat _O` —— 6/27 个有
- `CM_IntToFloat` —— 3/27 个有
- `Fast Groups Bypasser (rgthree)` —— 3/27 个有
- `ModelPatchTorchSettings` —— 3/27 个有
- `VHS_VideoCombine` —— 3/27 个有
- `DF_Int_to_Float` —— 2/27 个有
- `ImageFromBatch` —— 2/27 个有
- `ImpactSwitch` —— 2/27 个有
- `PreviewAny` —— 2/27 个有
- `Text Multiline` —— 2/27 个有
- `VHS_LoadVideo` —— 2/27 个有
- `llama_cpp_instruct_adv` —— 2/27 个有
- `llama_cpp_model_loader` —— 2/27 个有
- `llama_cpp_parameters` —— 2/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 27 | 100% |
| 采样算法 | er_sde | - | 27 | 100% |
| 调度器 | beta | - | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |
| 宽度 | 80 | 80 - 80 | 27 | 100% |
| 高度 | 80 | 80 - 80 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 35/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，27 个样本，一致性 100%
- 调度器 最常用 beta，27 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高发问题（35/27 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ShowAnything|Mie、intToFloat _O、CR Prompt Text
