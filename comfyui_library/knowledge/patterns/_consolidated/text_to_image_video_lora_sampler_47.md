---
name: text_to_image_video_lora_sampler_47
type: Text To Image
frequency: 13
level: strong
coverage: 0.881
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3视频参考编辑人物替换工作流，其它视频处理人物替换工具_2107176958315552769.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098819339918073857.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098820909527293953.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099181667595407361.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099549898831126529.json, 视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词T6工作流_角色一致性图生视频_2106097208906043393.json, 视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词，角色表演图生视频工作流_2103588976929099778.json, 视频生成/图生视频/MiniMax H3全参连续帧提示词自动优化工作流_图生视频高效创作方案_2106094286554099714.json, 视频生成/图生视频/MiniMax_H3去水印字幕图标加人物替换工作流，去水印其它视频处理方案_2109444784137003010.json, 视频生成/图生视频/MiniMax_H3视频参考编辑人物替换工作流，其它视频处理人物替换工具_2109455488231497729.json, 视频生成/图生视频/MinimaxH3 参考编辑人物替换 角色一致性更强_2104987281709953025.json, 视频生成/图生视频/MinimaxH3视频参考编辑T1版｜动作迁移人物替换一键搞定｜视频风格随心换_2104744951228755970.json, 视频生成/图生视频/MinimaxH3视频参考编辑人物替换T1｜视频图生视频换主角_2101905285496524802.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_47

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/MiniMax H3视频参考编辑人物替换工作流，其它视频处理人物替换工具_2107176958315552769.json、视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098819339918073857.json、视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098820909527293953.json、视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099181667595407361.json、视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099549898831126529.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 12/13 个有
- `SaveImage` —— 11/13 个有
- `easy showAnything` —— 11/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/13 个有
- `PreviewImage` —— 9/13 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 9/13 个有
- `Float to Int` —— 6/13 个有
- `GetVideoComponents` —— 6/13 个有
- `ImageConcatenate_UTK` —— 6/13 个有
- `ImageFromBatch` —— 6/13 个有
- `Int` —— 6/13 个有
- `LoadVideo` —— 6/13 个有
- `Video Duration Calculator` —— 6/13 个有
- `easy imageCount` —— 6/13 个有
- `easy indexAnything` —— 6/13 个有
- `easy mathInt` —— 6/13 个有
- `ExtractStoryboards_xuhuan1024` —— 5/13 个有
- `InspyrenetRembg` —— 5/13 个有
- `ImageResizeKJv2` —— 4/13 个有
- `MiniMaxH3ImageToVideo` —— 4/13 个有
- `EmptyImage` —— 3/13 个有
- `ResolutionSelector` —— 3/13 个有
- `ImageConcatenateMulti_UTK` —— 2/13 个有
- `FlashVSR_SM_KSampler` —— 1/13 个有
- `FlashVSR_SM_Model` —— 1/13 个有
- `JWInteger` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `LoadAudio` —— 1/13 个有
- `easy imageSplitGrid` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
