---
name: unknown_workflow_video_lora_sampler_161
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.761818
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, ImageScaleBy, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelSamplingSD3, Pick From Batch (mtb), Qwen3_VQA, SaveImage, Seed (rgthree), Text Concatenate, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1983048736781795330.json, 视频生成/图生视频/2033462929286242305.json, 视频生成/图生视频/1982721428191625217.json, 视频生成/图生视频/1998585239263961090.json, 视频生成/图生视频/1986359267705946114.json, 视频生成/图生视频/1986359186177093633.json, 视频生成/图生视频/1986492572971528194.json, 视频生成/图生视频/1987523064843931649.json, 视频生成/图生视频/2010958375034556418.json, 视频生成/图生视频/1986492511554334721.json, 视频生成/文生视频/Wan2.2 Smooth + Qwen3 VL反推扩写图生视频V2_1982707054148231169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_161

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1983048736781795330.json、视频生成/图生视频/2033462929286242305.json、视频生成/图生视频/1982721428191625217.json、视频生成/图生视频/1998585239263961090.json、视频生成/图生视频/1986359267705946114.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `Qwen3_VQA`
- `SaveImage`
- `Seed (rgthree)`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `WanImageToVideo` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `Any To Any` —— 8/11 个有
- `TT_img_enc` —— 8/11 个有
- `VHS_SelectFilename` —— 8/11 个有
- `TT_img_enc_v2` —— 7/11 个有
- `UnetLoaderGGUF` —— 6/11 个有
- `ColorMatch` —— 5/11 个有
- `PathchSageAttentionKJ` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `LayerUtility: PurgeVRAM` —— 4/11 个有
- `wanBlockSwap` —— 4/11 个有
- `AILab_QwenVL` —— 3/11 个有
- `RH_LLMAPI_NODE` —— 3/11 个有
- `ImageLoader` —— 2/11 个有
- `MultiplePathsInput` —— 2/11 个有
- `DuckHideNode` —— 1/11 个有
- `GetImageSizeAndCount` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `PainterI2V` —— 1/11 个有
- `WanFirstLastFrameToVideo` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 91% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 11 | 100% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler_ancestral | - | 11 | 100% |
| 重绘幅度 | simple | - | 11 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 91%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，11 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，11 个样本，一致性 100%
- 重绘幅度 最常用 simple，11 个样本，一致性 91%
