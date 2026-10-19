---
name: text_to_image_lora_sampler_clip_38
type: Text To Image
frequency: 16
level: strong
coverage: 0.902625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [ShowAnything|Mie, CR Prompt Text]
members: [视频生成/图生视频/MiniMax H3首尾帧加速版_图生视频运镜更流畅_2106610629435019266.json, 视频生成/图生视频/MiniMax H3首尾帧加速版｜图生视频出片更快更稳_2111084749388341249.json, 视频生成/图生视频/MiniMax H3首尾帧视频加速版，图生视频更流畅_2111203485525037057.json, 视频生成/图生视频/MiniMax+H3加速版图文一键生视频｜运镜丝滑出片快_2111327354969747458.json, 视频生成/图生视频/MiniMax_H3 I2V加速多参考生视频，高效图生视频工具_2110532068039028738.json, 视频生成/图生视频/MiniMax_H3_I2V加速多参考生视频，高效图生视频工具_2111269686322225154.json, 视频生成/图生视频/MiniMax_H3_I2V加速多参考视频生成工作流，图生视频高效创作工具_2109863281748963329.json, 视频生成/图生视频/MiniMax_H3_I2V加速首尾帧工作流，图生视频高效创作工具_2110535989906202626.json, 视频生成/图生视频/MiniMax_H3多图参考生成视频_图生视频与视频生视频全能参考方案_2106558188098248705.json, 视频生成/图生视频/MiniMax_H3多图参考生成视频图生视频与视频生视频全能参考方案_2109448439166750721.json, 视频生成/图生视频/MiniMax_H3多图参考生成视频，图生视频与视频生视频全能参考方案_2106558188098248705.json, 视频生成/图生视频/MiniMax_H3开源版首尾帧8步加速工作流，数字人图生视频处理工具_2109441379188436993.json, 视频生成/图生视频/MiniMax_H3角色替换工作流，文生视频视频生视频图生视频处理方案_2109459137858985985.json, 视频生成/图生视频/加速版MiniMax_H3图文直出视频｜一句话配一张图，成片一键拿_2099445108864282625.json, 视频生成/图生视频/加速版MiniMax_H3多参生视频｜图像音频一起喂，出片速度起飞_2099442755004096513.json, 视频生成/文生视频/MiniMax H3角色替换工作流，文生视频视频生视频图生视频处理方案_2107202145123659778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3首尾帧加速版_图生视频运镜更流畅_2106610629435019266.json、视频生成/图生视频/MiniMax H3首尾帧加速版｜图生视频出片更快更稳_2111084749388341249.json、视频生成/图生视频/MiniMax H3首尾帧视频加速版，图生视频更流畅_2111203485525037057.json、视频生成/图生视频/MiniMax+H3加速版图文一键生视频｜运镜丝滑出片快_2111327354969747458.json、视频生成/图生视频/MiniMax_H3 I2V加速多参考生视频，高效图生视频工具_2110532068039028738.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
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
- `PreviewImage` —— 12/16 个有
- `PrimitiveFloat` —— 11/16 个有
- `ResolutionSelector` —— 11/16 个有
- `SaveImage` —— 11/16 个有
- `EmptyImage` —— 10/16 个有
- `MiniMaxH3ImageToVideo` —— 10/16 个有
- `孤海注释` —— 10/16 个有
- `CR Prompt Text` —— 8/16 个有
- `EasyCache` —— 8/16 个有
- `PathchSageAttentionKJ` —— 8/16 个有
- `ShowAnything|Mie` —— 8/16 个有
- `PrimitiveStringMultiline` —— 7/16 个有
- `MiniMaxH3ReferenceToVideo` —— 6/16 个有
- `ImageResizeKJv2` —— 5/16 个有
- `Int` —— 5/16 个有
- `LoadAudio` —— 4/16 个有
- `CM_IntToFloat` —— 3/16 个有
- `DF_Int_to_Float` —— 3/16 个有
- `ImpactSwitch` —— 3/16 个有
- `ImageFromBatch` —— 2/16 个有
- `PreviewAny` —— 2/16 个有
- `Text Multiline` —— 2/16 个有
- `VHS_LoadVideo` —— 2/16 个有
- `intToFloat _O` —— 2/16 个有
- `llama_cpp_instruct_adv` —— 2/16 个有
- `llama_cpp_model_loader` —— 2/16 个有
- `llama_cpp_parameters` —— 2/16 个有
- `GetVideoComponents` —— 1/16 个有
- `LoadVideo` —— 1/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/16 个有

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
| Steps较低可能导致细节不足 | 20/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（20/16 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ShowAnything|Mie、CR Prompt Text
