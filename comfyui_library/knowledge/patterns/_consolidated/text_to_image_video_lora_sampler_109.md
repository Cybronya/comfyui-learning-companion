---
name: text_to_image_video_lora_sampler_109
type: Text To Image
frequency: 6
level: strong
coverage: 0.881167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Float to Int, GetVideoComponents, ImageConcatenate_UTK, ImageFromBatch, Int, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PreviewImage, PrimitiveFloat, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, Video Duration Calculator, easy MiniMaxH3ReferenceToVideoBridge, easy imageCount, easy mathInt, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3视频参考编辑人物替换工作流，其它视频处理人物替换工具_2107176958315552769.json, 视频生成/图生视频/MiniMax_H3去水印字幕图标加人物替换工作流，去水印其它视频处理方案_2109444784137003010.json, 视频生成/图生视频/MiniMax_H3视频参考编辑人物替换工作流，其它视频处理人物替换工具_2109455488231497729.json, 视频生成/图生视频/MinimaxH3 参考编辑人物替换 角色一致性更强_2104987281709953025.json, 视频生成/图生视频/MinimaxH3视频参考编辑T1版｜动作迁移人物替换一键搞定｜视频风格随心换_2104744951228755970.json, 视频生成/图生视频/MinimaxH3视频参考编辑人物替换T1｜视频图生视频换主角_2101905285496524802.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_109

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/MiniMax H3视频参考编辑人物替换工作流，其它视频处理人物替换工具_2107176958315552769.json、视频生成/图生视频/MiniMax_H3去水印字幕图标加人物替换工作流，去水印其它视频处理方案_2109444784137003010.json、视频生成/图生视频/MiniMax_H3视频参考编辑人物替换工作流，其它视频处理人物替换工具_2109455488231497729.json、视频生成/图生视频/MinimaxH3 参考编辑人物替换 角色一致性更强_2104987281709953025.json、视频生成/图生视频/MinimaxH3视频参考编辑T1版｜动作迁移人物替换一键搞定｜视频风格随心换_2104744951228755970.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Float to Int`
- `GetVideoComponents`
- `ImageConcatenate_UTK`
- `ImageFromBatch`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PreviewImage`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `Video Duration Calculator`
- `easy MiniMaxH3ReferenceToVideoBridge`
- `easy imageCount`
- `easy mathInt`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ExtractStoryboards_xuhuan1024` —— 5/6 个有
- `InspyrenetRembg` —— 5/6 个有
- `easy indexAnything` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `SaveImage` —— 4/6 个有
- `EmptyImage` —— 3/6 个有
- `FlashVSR_SM_KSampler` —— 1/6 个有
- `FlashVSR_SM_Model` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
