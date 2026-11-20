---
name: unknown_workflow_video_lora_sampler_329
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.926
common_nodes: [Any To Any, BerniniConditioning, CLIPLoader, CLIPTextEncode, CR Prompt Text, CreateVideo, GetVideoComponents, HunyuanVideoFoley, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, Qwen3_VQA, SaveVideo, StringReplace, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Bernini 视频生成与“多镜头导演台”_支持配音_2065695983807320066.json, 图片生成/图生图/（4步加速、提示词扩写版）Bernini图生视频+音效V4_2077326857673990145.json, 视频生成/图生视频/Bernini导演台多参音画同步简约版V3（乱神-循环版）_2065331654767505409.json, 视频生成/图生视频/Bernini导演台多参音画同步简约版V3（乱神-循环版）_2065702680814776322.json, 视频生成/图生视频/数字人Bernini图生视频 YC Foley音效 音视频生成 数字人说话唱歌 带运镜参考_2067419048618577922.json, 视频生成/图生视频/（4步加速版）Bernini图生视频+音效V4_2073466231541293057.json, 视频生成/图生视频/（4步加速版）Bernini导演台多参音画同步简约版V3（乱神-循环版）_2073465859552669698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_329

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Bernini 视频生成与“多镜头导演台”_支持配音_2065695983807320066.json、图片生成/图生图/（4步加速、提示词扩写版）Bernini图生视频+音效V4_2077326857673990145.json、视频生成/图生视频/Bernini导演台多参音画同步简约版V3（乱神-循环版）_2065331654767505409.json、视频生成/图生视频/Bernini导演台多参音画同步简约版V3（乱神-循环版）_2065702680814776322.json、视频生成/图生视频/数字人Bernini图生视频 YC Foley音效 音视频生成 数字人说话唱歌 带运镜参考_2067419048618577922.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `Any To Any`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CreateVideo`
- `GetVideoComponents`
- `HunyuanVideoFoley`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `SaveVideo`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BerniniPromptEnhancer` —— 6/7 个有
- `RHLLMChatNode` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `easy batchAnything` —— 4/7 个有
- `easy forLoopEnd` —— 4/7 个有
- `easy forLoopStart` —— 4/7 个有
- `easy mergeVideosFromPaths` —— 4/7 个有
- `easy timelineEditor` —— 4/7 个有
- `easy timelineInfoOutput` —— 4/7 个有
- `easy timelineSegmentCount` —— 4/7 个有
- `easy timelineSegmentOutput` —— 4/7 个有
- `JWInteger` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `LoadImage` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `Text` —— 3/7 个有
- `easy imagesSplitImage` —— 3/7 个有
- `PreviewAny` —— 2/7 个有
- `llama_cpp_instruct_adv` —— 2/7 个有
- `llama_cpp_model_loader` —— 2/7 个有
- `llama_cpp_parameters` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 10 | 4 - 10 | 7 | 60% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 4 - 10，7 个样本
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
