---
name: unknown_workflow_video_lora_sampler_374
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.760667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, Seed (rgthree), Text Concatenate, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/视频_1999314736896503810.json, 视频生成/图生视频/（官方版）Wan2.2 Remix V2+Qwen3 VL扩写图生视频V1_1986492572971528194.json, 视频生成/图生视频/（官方版）Wan2.2+Remix+V2+Qwen3+VL扩写图生视频V1 (1)_1987523064843931649.json, 视频生成/图生视频/（官方版）Wan2.2+Remix+V2+Qwen3.5扩写图生视频V1 (1)_2042534334439100418.json, 视频生成/图生视频/（自用）Wan2.2 Remix V2.1高噪+2.0低噪PainterI2V自动提示词图生视频_2010958375034556418.json, 视频生成/图生视频/（（自用）-官方版）Wan2.2 Remix V2+Qwen3图生视频V1_1986492511554334721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_374

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/视频_1999314736896503810.json、视频生成/图生视频/（官方版）Wan2.2 Remix V2+Qwen3 VL扩写图生视频V1_1986492572971528194.json、视频生成/图生视频/（官方版）Wan2.2+Remix+V2+Qwen3+VL扩写图生视频V1 (1)_1987523064843931649.json、视频生成/图生视频/（官方版）Wan2.2+Remix+V2+Qwen3.5扩写图生视频V1 (1)_2042534334439100418.json、视频生成/图生视频/（自用）Wan2.2 Remix V2.1高噪+2.0低噪PainterI2V自动提示词图生视频_2010958375034556418.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Seed (rgthree)`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 5/6 个有
- `ImageScaleBy` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 5/6 个有
- `Pick From Batch (mtb)` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `Qwen3_VQA` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `WanImageToVideo` —— 5/6 个有
- `Any To Any` —— 4/6 个有
- `VHS_SelectFilename` —— 4/6 个有
- `AILab_QwenVL` —— 3/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `TT_img_enc` —— 2/6 个有
- `TT_img_enc_v2` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `CompressImages` —— 1/6 个有
- `DuckHideNode` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有
- `PainterI2V` —— 1/6 个有
- `ShellAgentPluginOutputText` —— 1/6 个有
- `easy anythingIndexSwitch` —— 1/6 个有
- `easy int` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有
- `llama_cpp_parameters` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler_ancestral | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
