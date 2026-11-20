---
name: unknown_workflow_clip_unet_vae_5
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.821
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux_Klein_替换背景_替换场景_2013595653783425025.json, 图片生成/图生图/YJ-flux2-高清无损放大_2060924553131544578.json, 图片生成/图生图/klein双采样调色（附有专用提示词）_2056177072564916226.json, 图片生成/图生图/klein超清质感修复_2060928049100709889.json, 图片生成/图生图/klein超清质感修复_2093886165723209730.json, 图片生成/图生图/klein超清质感修复_2093906745293885442.json, 图片生成/图生图/去ai感洗图_真人写实超清皮肤纹理_2061272397898145793.json, 图片生成/图生图/图像放大（Klein+Seedvr2）_2027275378363994113.json, 图片生成/图生图/皮肤修复 klein无塑料感高清修复_2061013101813788674.json, 图片生成/文生图/节点系列04-Fast Groups Bypasser (rgthree)节点介绍_2028724362504839170.json, 平台全量/Flux2多图编辑_2015708848413216769.json, 平台全量/Klein高一致性动漫转真人+过审加密+Seedvr2放大4K_2035395027601461249.json, 平台全量/Klein高一致性动漫转真人v2+过审加密+Seedvr2放大4K_2046468855819673601.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Flux_Klein_替换背景_替换场景_2013595653783425025.json、图片生成/图生图/YJ-flux2-高清无损放大_2060924553131544578.json、图片生成/图生图/klein双采样调色（附有专用提示词）_2056177072564916226.json、图片生成/图生图/klein超清质感修复_2060928049100709889.json、图片生成/图生图/klein超清质感修复_2093886165723209730.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 12/13 个有
- `SeedVR2LoadDiTModel` —— 9/13 个有
- `SeedVR2LoadVAEModel` —— 9/13 个有
- `SeedVR2VideoUpscaler` —— 9/13 个有
- `easy imageColorMatch` —— 9/13 个有
- `ImageResizeKJv2` —— 8/13 个有
- `KSamplerAdvanced` —— 8/13 个有
- `PreviewImage` —— 7/13 个有
- `CFGGuider` —— 5/13 个有
- `EmptyFlux2LatentImage` —— 5/13 个有
- `Flux2Scheduler` —— 5/13 个有
- `KSamplerSelect` —— 5/13 个有
- `RandomNoise` —— 5/13 个有
- `SamplerCustomAdvanced` —— 5/13 个有
- `Fast Groups Bypasser (rgthree)` —— 3/13 个有
- `Fast Groups Muter (rgthree)` —— 3/13 个有
- `ImageScaleToTotalPixels` —— 3/13 个有
- `LayerUtility: PurgeVRAM` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `DuckHideNode` —— 2/13 个有
- `GetImageSize` —— 2/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `Lora Loader Stack (rgthree)` —— 2/13 个有
- `LoraLoaderModelOnly` —— 2/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `easy getNode` —— 2/13 个有
- `easy imageConcat` —— 2/13 个有
- `easy setNode` —— 2/13 个有
- `LatentBlend` —— 1/13 个有
- `LayerColor: Brightness & Contrast` —— 1/13 个有
- `ShowText|pysssss` —— 1/13 个有
- `Text` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 62% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | sa_solver | - | 8 | 75% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 8 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，8 个样本，一致性 75%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，8 个样本，一致性 75%
