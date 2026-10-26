---
name: unknown_workflow_video_lora_sampler_676
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.729667
common_nodes: [Any Switch (rgthree), Any To Any, BatchImagesNode, BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, CR Prompt Text, CreateVideo, Fast Groups Bypasser (rgthree), GetNode, GetVideoComponents, HunyuanVideoFoley, ImageResizeKJv2, JWInteger, JsonExtractString, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveInt, PurgeVRAM_UTK, Qwen3_VQA, RH_LLMAPI_Pro_Node, SaveVideo, SetNode, StringReplace, Text, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, ratio_selector, string_util_StrConcat]
problems: []
missing: []
members: [视频生成/图生视频/Bernini角色三视图加场景参考生视频-4步加速-VBVR增强-自动配音效V1_2073785821202833409.json, 视频生成/图生视频/Bernini角色三视图加场景参考生视频-自动配音效V2_2064710909074952193.json, 视频生成/图生视频/Bernini首尾帧生视频V1_2074031023091965954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_676

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Bernini角色三视图加场景参考生视频-4步加速-VBVR增强-自动配音效V1_2073785821202833409.json、视频生成/图生视频/Bernini角色三视图加场景参考生视频-自动配音效V2_2064710909074952193.json、视频生成/图生视频/Bernini首尾帧生视频V1_2074031023091965954.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Any To Any`
- `BatchImagesNode`
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetVideoComponents`
- `HunyuanVideoFoley`
- `ImageResizeKJv2`
- `JWInteger`
- `JsonExtractString`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PurgeVRAM_UTK`
- `Qwen3_VQA`
- `RH_LLMAPI_Pro_Node`
- `SaveVideo`
- `SetNode`
- `StringReplace`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ratio_selector`
- `string_util_StrConcat`

**可变部分**（部分 workflow 才有）：
- `GroupSwitcher` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 10 | 3 | 53% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 10，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
