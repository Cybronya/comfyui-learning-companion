---
name: unknown_workflow_video_lora_sampler_101
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.891933
common_nodes: [Any To Any, BerniniConditioning, CLIPLoader, CLIPTextEncode, CR Prompt Text, CreateVideo, GetVideoComponents, HunyuanVideoFoley, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, Qwen3_VQA, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2065427279056031745.json, 视频生成/图生视频/2073849977520087042.json, 视频生成/图生视频/2073573407953874946.json, 视频生成/图生视频/2065620056792457217.json, 视频生成/图生视频/Bernini图生视频+YC Foley音效音视频生成_2065776899741278209.json, 视频生成/图生视频/2065425977529950209.json, 视频生成/图生视频/2064963434780905474.json, 视频生成/图生视频/2065053728595599362.json, 视频生成/图生视频/2064182035551440898.json, 视频生成/图生视频/2064632452102053889.json, 视频生成/图生视频/2064237198987321346.json, 视频生成/图生视频/2064364509602603010.json, 视频生成/图生视频/Images to Video Bernini图生视频+YC+Foley音效Sound Effect_2097160102343172098.json, 视频生成/图生视频/Images to Video+Bernini图生视频+YC+Foley音效Sound+Effect_2104029726410100737.json, 视频生成/图生视频/2073970025681219585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_101

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/2065427279056031745.json、视频生成/图生视频/2073849977520087042.json、视频生成/图生视频/2073573407953874946.json、视频生成/图生视频/2065620056792457217.json、视频生成/图生视频/Bernini图生视频+YC Foley音效音视频生成_2065776899741278209.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
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
- `BerniniPromptEnhancer` —— 14/15 个有
- `StringReplace` —— 14/15 个有
- `easy showAnything` —— 14/15 个有
- `PrimitiveInt` —— 13/15 个有
- `SaveVideo` —— 13/15 个有
- `Text` —— 13/15 个有
- `RHLLMChatNode` —— 12/15 个有
- `SimpleMath+` —— 3/15 个有
- `BatchImagesNode` —— 2/15 个有
- `ImageResizeKJv2` —— 2/15 个有
- `Int` —— 2/15 个有
- `RH_LLMAPI_NODE` —— 2/15 个有
- `ACE_AudioCrop` —— 1/15 个有
- `AdjustAudio` —— 1/15 个有
- `Audio Add Silence` —— 1/15 个有
- `AudioCombine` —— 1/15 个有
- `GetNode` —— 1/15 个有
- `JjkText` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `LoadAudio` —— 1/15 个有
- `Primitive integer [Crystools]` —— 1/15 个有
- `RH_Translator` —— 1/15 个有
- `RunningHub_VoxCPM_Generate` —— 1/15 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/15 个有
- `SaveAudio` —— 1/15 个有
- `SetNode` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 15 | 100% |
| Prompt 约束强度(CFG) | 10 | 4 - 10 | 15 | 73% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | euler | - | 15 | 100% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，15 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 4 - 10，15 个样本
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，15 个样本，一致性 100%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
