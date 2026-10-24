---
name: unknown_workflow_video_lora_sampler_47
type: Unknown Workflow
frequency: 21
level: strong
coverage: 0.907095
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DF_Integer, ImageStitch, KSamplerAdvanced, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, RH_Captioner, RH_Translator, SimpleMath+, UNETLoader, VAEDecode, VAELoader, WanFirstLastFrameToVideo, WanVideoNAG, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/wan2.2首尾帧（优化版官方）_1980173041701392386.json, 图片生成/图生图/逼真手办全能图片V1香蕉新模型_1960722587741556737.json, 视频生成/图生视频/wan2.2首尾 版官方_1952339456634368002.json, 视频生成/图生视频/wan2.2首尾帧优化版_1956153773183959042.json, 视频生成/图生视频/wan2.2首尾帧视频-傲雪AIGC_1962136836984475650.json, 视频生成/图生视频/wan2.2首尾帧（优化版官方）_1951973819386900481.json, 视频生成/图生视频/wan2.2首尾帧（优化版官方）_1952239777980600322.json, 视频生成/图生视频/wan2.2首尾帧（优化版官方）_1952981780628443138.json, 视频生成/图生视频/wan2.2首尾帧（优化版官方）_1967782938588884994.json, 视频生成/图生视频/wan2.2首尾帧（优化版官方）_2004156685763731458.json, 视频生成/图生视频/wan2.2首尾帧（优化版官方）_2015306300099403777.json, 视频生成/图生视频/wan2.2首尾帧（优化版官方）_2054766656261500930.json, 视频生成/图生视频/wan2.2首尾帧（优化版官方）_2055193435040165889.json, 视频生成/图生视频/wan2.2首尾帧（优化版官方）_2072861343484567553.json, 视频生成/图生视频/全能图片V1+wan2.2-变老特效-图生视频-视频补帧放大_1962663438763864066.json, 视频生成/图生视频/全能图片V1+wan2.2-变胖特效-图生视频-视频补帧放大_1962700232851079170.json, 视频生成/图生视频/全能图片V1+wan2.2-跳舞视频-图生视频-视频补帧放大_1962711139945693186.json, 视频生成/图生视频/可爱表情包_1980870124980883457.json, 视频生成/图生视频/首尾帧图生视频lightx2v + wan2.2_1953264149745889282.json, 视频生成/文生视频/wan2.2 首尾帧视频_1957693851249078273.json, 视频生成/文生视频/wan2.2首尾帧（优化版官方）_1957688772295061505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_47

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/wan2.2首尾帧（优化版官方）_1980173041701392386.json、图片生成/图生图/逼真手办全能图片V1香蕉新模型_1960722587741556737.json、视频生成/图生视频/wan2.2首尾 版官方_1952339456634368002.json、视频生成/图生视频/wan2.2首尾帧优化版_1956153773183959042.json、视频生成/图生视频/wan2.2首尾帧视频-傲雪AIGC_1962136836984475650.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DF_Integer`
- `ImageStitch`
- `KSamplerAdvanced`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_Captioner`
- `RH_Translator`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanFirstLastFrameToVideo`
- `WanVideoNAG`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 20/21 个有
- `Textbox` —— 20/21 个有
- `easy ifElse` —— 20/21 个有
- `CreateVideo` —— 18/21 个有
- `SaveVideo` —— 18/21 个有
- `PreviewImage` —— 5/21 个有
- `RH_Nano_Banana_Image2Image` —— 5/21 个有
- `VHS_VideoCombine` —— 4/21 个有
- `CR Upscale Image` —— 3/21 个有
- `RIFE VFI` —— 3/21 个有
- `CR Text` —— 1/21 个有
- `ImageConcanate` —— 1/21 个有
- `ImageScale` —— 1/21 个有
- `Int` —— 1/21 个有
- `PlaySound|pysssss` —— 1/21 个有
- `RH_LLMAPI_NODE` —— 1/21 个有
- `SaveImage` —— 1/21 个有
- `Text Multiline` —— 1/21 个有
- `TextCombinerSix` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 21 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 21 | 100% |
| 采样算法 | 4 | 4 - 4 | 21 | 100% |
| 调度器 | euler | - | 21 | 100% |
| 重绘幅度 | simple | - | 21 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，21 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，21 个样本，取值集中（一致性 100%）
- 采样算法 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，21 个样本，一致性 100%
- 重绘幅度 最常用 simple，21 个样本，一致性 100%
