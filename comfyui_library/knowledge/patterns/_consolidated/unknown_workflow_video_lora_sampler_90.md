---
name: unknown_workflow_video_lora_sampler_90
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.890875
common_nodes: [Any To Any, BerniniConditioning, CLIPLoader, CLIPTextEncode, CR Prompt Text, CreateVideo, GetVideoComponents, HunyuanVideoFoley, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, Qwen3_VQA, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Bemini图生视频_2065427279056031745.json, 视频生成/图生视频/Bernini  电商视频 生成  只消耗 RH币  开plus 运行_2073849977520087042.json, 视频生成/图生视频/Bernini参考人物图生视频+音效V整理版（转自T8大佬）_2073573407953874946.json, 视频生成/图生视频/Bernini图生视频+YC Foley音效  音视频生成  数字人说话唱歌 带运镜参考_2065620056792457217.json, 视频生成/图生视频/Bernini图生视频+YC Foley音效音视频生成_2065776899741278209.json, 视频生成/图生视频/Bernini图生视频+YC Foley音效（一站式音视频生成方案）_2065425977529950209.json, 视频生成/图生视频/Bernini图生视频+配音音效V2+自动提示词_2064963434780905474.json, 视频生成/图生视频/Bernini图生视频+音效V2_2065053728595599362.json, 视频生成/图生视频/Bernini图生视频+音效V3_2064182035551440898.json, 视频生成/图生视频/Bernini图生视频+音效【开源Seedance】_2064632452102053889.json, 视频生成/图生视频/Bernini多图参考生视频+音效V3_2064237198987321346.json, 视频生成/图生视频/Bernini自动提示词图生视频+音效V3_2064364509602603010.json, 视频生成/图生视频/Images to Video Bernini图生视频+YC+Foley音效Sound Effect_2097160102343172098.json, 视频生成/图生视频/Images to Video+Bernini图生视频+YC+Foley音效Sound+Effect_2104029726410100737.json, 视频生成/图生视频/开源最强全模态图生视频：背景音效+单人内心独白_2073970025681219585.json, 视频生成/图生视频/（4步加速版）Bernini多图参考生视频+音效V4_2073466320544423937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_90

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/Bemini图生视频_2065427279056031745.json、视频生成/图生视频/Bernini  电商视频 生成  只消耗 RH币  开plus 运行_2073849977520087042.json、视频生成/图生视频/Bernini参考人物图生视频+音效V整理版（转自T8大佬）_2073573407953874946.json、视频生成/图生视频/Bernini图生视频+YC Foley音效  音视频生成  数字人说话唱歌 带运镜参考_2065620056792457217.json、视频生成/图生视频/Bernini图生视频+YC Foley音效音视频生成_2065776899741278209.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `Any To Any`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CreateVideo`
- `GetVideoComponents`
- `HunyuanVideoFoley`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BerniniPromptEnhancer` —— 15/16 个有
- `StringReplace` —— 15/16 个有
- `easy showAnything` —— 15/16 个有
- `PrimitiveInt` —— 14/16 个有
- `SaveVideo` —— 14/16 个有
- `Text` —— 14/16 个有
- `RHLLMChatNode` —— 13/16 个有
- `BatchImagesNode` —— 3/16 个有
- `ImageResizeKJv2` —— 3/16 个有
- `SimpleMath+` —— 3/16 个有
- `Int` —— 2/16 个有
- `RH_LLMAPI_NODE` —— 2/16 个有
- `ACE_AudioCrop` —— 1/16 个有
- `AdjustAudio` —— 1/16 个有
- `Audio Add Silence` —— 1/16 个有
- `AudioCombine` —— 1/16 个有
- `GetNode` —— 1/16 个有
- `JjkText` —— 1/16 个有
- `Label (rgthree)` —— 1/16 个有
- `LoadAudio` —— 1/16 个有
- `Primitive integer [Crystools]` —— 1/16 个有
- `RH_Translator` —— 1/16 个有
- `RunningHub_VoxCPM_Generate` —— 1/16 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/16 个有
- `SaveAudio` —— 1/16 个有
- `SetNode` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 16 | 100% |
| Prompt 约束强度(CFG) | 10 | 4 - 10 | 16 | 69% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | euler | - | 16 | 100% |
| 重绘幅度 | simple | - | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，16 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 4 - 10，16 个样本
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，16 个样本，一致性 100%
- 重绘幅度 最常用 simple，16 个样本，一致性 100%
