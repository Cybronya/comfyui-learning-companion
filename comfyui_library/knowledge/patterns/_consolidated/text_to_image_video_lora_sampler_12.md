---
name: text_to_image_video_lora_sampler_12
type: Text To Image
frequency: 32
level: strong
coverage: 0.886437
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Float to Int, GetVideoComponents, ImageConcatenate_UTK, ImageFromBatch, Int, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadVideo, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, Video Duration Calculator, easy MiniMaxH3ReferenceToVideoBridge, easy imageCount, easy mathInt, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3全参模式角色替换 视频处理工具_2100634529659711490.json, 图片生成/图生图/H3视频参考编辑人物换装处理生成工具包集_2100281577153585154.json, 图片生成/图生图/H3视频编辑去除人物 视频处理生成工具包_2100283161178624002.json, 图片生成/图生图/MiniMax H3视频参考编辑人物替换工作流，其它视频处理人物替换工具_2107176958315552769.json, 图片生成/图生图/MiniMaxH3视频参考编辑｜人物换装视频处理_2095566743472271362.json, 图片生成/图生图/MiniMaxH3视频编辑去人物｜擦除人物视频处理_2095565407036985345.json, 图片生成/图生图/Minimax3全参模式角色替换｜其它视频处理也能这么玩，换脸换人一气呵成_2100429176577806338.json, 图片生成/图生图/Minimax3全参模式角色替换｜参考图加原视频视频处理_2088763480580120578.json, 图片生成/图生图/Minimax3全参模式｜视频角色替换高质量处理_2095928159500857346.json, 图片生成/图生图/MinimaxH3视频参考编辑人物替换T1｜其它视频处理利器_2106972577502679041.json, 图片生成/图生图/MinimaxH3视频编辑V1｜一键去除视频背景里多余人物｜画面瞬间干净_2099118326118174721.json, 图片生成/图生图/MinimaxH3视频编辑去除人物2｜视频处理一键擦除_2100793280198955009.json, 图片生成/图生图/minimaxH3视频编辑复刻｜抖音热门特效V1直出_2092010345916354562.json, 图片生成/图生图/人物替换T1｜MinimaxH3视频参考编辑，换主角不影响背景_2099916510587351042.json, 图片生成/图生图/人物替换参考视频编辑｜MinimaxH3视频处理T1版_2095797239611478017.json, 图片生成/图生图/全参模式角色替换实操｜Minimax3 视频处理新玩法_2096202523513286657.json, 图片生成/图生图/全参模式角色替换｜Minimax3其它视频处理_2092565834769190913.json, 图片生成/图生图/抖音热门特效V1复刻｜minimaxH3视频编辑轻松上手_2096212199453847553.json, 图片生成/图生图/背景人物一键去除｜MinimaxH3视频编辑V1_2091162669549182978.json, 图片生成/图生图/背景人物去除编辑｜MinimaxH3视频V1处理工作流_2095133128032612354.json, 图片生成/图生图/视频参考编辑人物换装｜MinimaxH3其它视频处理工作流_2087192449147031554.json, 图片生成/图生图/视频参考编辑人物替换T1｜MinimaxH3其它视频处理工作流_2087196055795490818.json, 图片生成/图生图/视频参考编辑人物替换｜MinimaxH3视频处理T1直出_2091586865601277954.json, 图片生成/图生图/视频杂物清道夫｜MinimaxH3一键去除多余人物元素_2096518368504410114.json, 图片生成/图生图/视频编辑一键去除人物｜MinimaxH3其它视频处理_2095793371834048514.json, 图片生成/图生图/视频编辑去人物2｜MinimaxH3其它视频处理_2092909484829134850.json, 图片生成/图生图/视频编辑去除多余人物｜MinimaxH3画面擦除处理_2096293888435769346.json, 视频生成/图生视频/MiniMax_H3去水印字幕图标加人物替换工作流，去水印其它视频处理方案_2109444784137003010.json, 视频生成/图生视频/MiniMax_H3视频参考编辑人物替换工作流，其它视频处理人物替换工具_2109455488231497729.json, 视频生成/图生视频/MinimaxH3 参考编辑人物替换 角色一致性更强_2104987281709953025.json, 视频生成/图生视频/MinimaxH3视频参考编辑T1版｜动作迁移人物替换一键搞定｜视频风格随心换_2104744951228755970.json, 视频生成/图生视频/MinimaxH3视频参考编辑人物替换T1｜视频图生视频换主角_2101905285496524802.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（图片生成/图生图/H3全参模式角色替换 视频处理工具_2100634529659711490.json、图片生成/图生图/H3视频参考编辑人物换装处理生成工具包集_2100281577153585154.json、图片生成/图生图/H3视频编辑去除人物 视频处理生成工具包_2100283161178624002.json、图片生成/图生图/MiniMax H3视频参考编辑人物替换工作流，其它视频处理人物替换工具_2107176958315552769.json、图片生成/图生图/MiniMaxH3视频参考编辑｜人物换装视频处理_2095566743472271362.json…）

- **类型**：Text To Image
- **样本数**：32
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 32 个 workflow 都包含：
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
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
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
- `孤海注释` —— 31/32 个有
- `PreviewImage` —— 24/32 个有
- `Text` —— 24/32 个有
- `ExtractStoryboards_xuhuan1024` —— 23/32 个有
- `LoadImage` —— 22/32 个有
- `easy indexAnything` —— 13/32 个有
- `CR Image Grid Panel` —— 10/32 个有
- `InspyrenetRembg` —— 10/32 个有
- `FlashVSR_SM_KSampler` —— 9/32 个有
- `FlashVSR_SM_Model` —— 9/32 个有
- `JWInteger` —— 9/32 个有
- `LayerUtility: PurgeVRAM V2` —— 9/32 个有
- `SaveImage` —— 6/32 个有
- `EmptyImage` —— 3/32 个有
- `RH_RhartImageG2OfficialImageToImage` —— 3/32 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 32 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 32 | 100% |
| 采样算法 | er_sde | - | 32 | 100% |
| 调度器 | beta | - | 32 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 32 | 100% |
| 宽度 | 80 | 80 - 80 | 32 | 100% |
| 高度 | 80 | 80 - 80 | 32 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 32/32 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，32 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，32 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，32 个样本，一致性 100%
- 调度器 最常用 beta，32 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，32 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，32 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，32 个样本，取值集中（一致性 100%）
- 高发问题（32/32 个样本）：Steps较低可能导致细节不足
