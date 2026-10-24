---
name: unknown_workflow_video_sampler_clip_26
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.740875
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ColorMatch, ImageResizeKJv2, ImageScaleBy, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, Pick From Batch (mtb), PreviewImage, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Comfy挑战赛-Smooth图生视频_2057652763391258625.json, 图片生成/图生图/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2029916808320389121.json, 图片生成/图生图/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2031365125562703874.json, 视频生成/图生视频/Dasiwa I2V图生视频自动提示词工作流V1（动态加强）_1991465239868817409.json, 视频生成/图生视频/Dasiwa V10 Vs V9 + Qwen3.5多重对比I2V_2040996978963783681.json, 视频生成/图生视频/Dasiwa V9+PainterI2V图生视频自动提示词工作流V1（写实强化版）_2013524441493413889.json, 视频生成/图生视频/Dasiwa V9+PainterI2V图生视频自动提示词工作流V1（动漫强化版）_2011778743831896065.json, 视频生成/图生视频/Remix V3 + Qwen3.5多重对比I2V_2035642798367580161.json, 视频生成/图生视频/Wan2.2 Dasiwa V10+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2040996941684805634.json, 视频生成/图生视频/Wan2.2 Dasiwa V10+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2041144753068183554.json, 视频生成/图生视频/Wan2.2 Dasiwa V10+Qwen3.5自动化图生视频V1（逻辑动态加强版）对镜自拍_2041411103518887938.json, 视频生成/图生视频/Wan2.2 Remix V3.0+Qwen3.5图生视频_2037879227361533953.json, 视频生成/图生视频/Wan2.2 Remix V3.0+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2035642836963565570.json, 视频生成/图生视频/Wan2.2 Remix V3.0+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2036976880821215234.json, 视频生成/图生视频/Wan2.2 Remix V3.0+Qwen3.5自动化图生视频V1（逻辑动态加强版）_2062141489110667266.json, 视频生成/图生视频/Wan2.2图生视频、自动生成视频脚本_2041400574976991233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Comfy挑战赛-Smooth图生视频_2057652763391258625.json、图片生成/图生图/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2029916808320389121.json、图片生成/图生图/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2031365125562703874.json、视频生成/图生视频/Dasiwa I2V图生视频自动提示词工作流V1（动态加强）_1991465239868817409.json、视频生成/图生视频/Dasiwa V10 Vs V9 + Qwen3.5多重对比I2V_2040996978963783681.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ColorMatch`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Float` —— 15/16 个有
- `ImageFromBatch+` —— 15/16 个有
- `LayerUtility: PurgeVRAM` —— 15/16 个有
- `MathExpression|pysssss` —— 15/16 个有
- `PainterI2V` —— 15/16 个有
- `PathchSageAttentionKJ` —— 15/16 个有
- `RunningHub Deepcleaner` —— 15/16 个有
- `CR Prompt Text` —— 14/16 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 14/16 个有
- `easy anythingIndexSwitch` —— 13/16 个有
- `CR Text` —— 10/16 个有
- `ShellAgentPluginOutputText` —— 10/16 个有
- `llama_cpp_instruct_adv` —— 10/16 个有
- `llama_cpp_model_loader` —— 10/16 个有
- `llama_cpp_parameters` —— 10/16 个有
- `AILab_QwenVL` —— 5/16 个有
- `RH_LLMAPI_NODE` —— 5/16 个有
- `LoraLoaderModelOnly` —— 4/16 个有
- `AddLabel` —— 2/16 个有
- `ImageConcanate` —— 2/16 个有
- `ProcessString` —— 2/16 个有
- `WanImageToVideo` —— 2/16 个有
- `Int` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有
- `RIFE VFI` —— 1/16 个有
- `StringConcatenate` —— 1/16 个有
- `UnetLoaderGGUF` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 16 | 94% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 16 | 100% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | euler_ancestral | - | 16 | 94% |
| 重绘幅度 | simple | - | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，16 个样本，一致性 94%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，16 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，16 个样本，一致性 94%
- 重绘幅度 最常用 simple，16 个样本，一致性 100%
