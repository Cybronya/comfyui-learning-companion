---
name: text_to_image_sampler_clip_unet_34
type: Text To Image
frequency: 14
level: moderate
coverage: 0.950214
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/3D相机360自由转角度Qwen Multiangle Camera_2010324164619538433.json, 图片生成/图生图/3D相机360自由转角度Qwen Multiangle Camera_2011543783875289089.json, 图片生成/图生图/3D角度_2043970024796332034.json, 图片生成/图生图/ComfyUI_qwen_image_edit_plus_1970668113702363137.json, 图片生成/图生图/ComfyUI_qwen_image_edit_plus_2029745752934715394.json, 图片生成/图生图/Krea2-无提示词洗图工作流_2074826967077187586.json, 图片生成/图生图/Krea2-深度控制_2074499977073750018.json, 图片生成/图生图/Qwen千问2511多角度分镜生成(产品物体摄影等)3D相机 360自由转角度工作流_2010889062151884801.json, 图片生成/图生图/qwen_image 多视图 三视图 多角度 视觉角度控制器_2036336395916156929.json, 图片生成/图生图/可视化编辑视角_2032127067772424194.json, 图片生成/图生图/洗图 反推 提示词 qwen_image_edit_2511_2043323150406000641.json, 图片生成/图生图/洗图 反推 提示词 qwen_image_edit_2511_2043521965289381889.json, 图片生成/图生图/洗图 反推 提示词 qwen_image_edit_2511_2043522576344948738.json, 图片生成/图生图/角度控制  视觉控制  视图控制 角度调整_2095375897426747394.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_34

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/3D相机360自由转角度Qwen Multiangle Camera_2010324164619538433.json、图片生成/图生图/3D相机360自由转角度Qwen Multiangle Camera_2011543783875289089.json、图片生成/图生图/3D角度_2043970024796332034.json、图片生成/图生图/ComfyUI_qwen_image_edit_plus_1970668113702363137.json、图片生成/图生图/ComfyUI_qwen_image_edit_plus_2029745752934715394.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 13/14 个有
- `LoraLoaderModelOnly` —— 10/14 个有
- `PreviewImage` —— 10/14 个有
- `QwenMultiangleCameraNode` —— 10/14 个有
- `LayerUtility: ImageReel` —— 7/14 个有
- `LayerUtility: ImageReelComposit` —— 7/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/14 个有
- `easy imageSize` —— 6/14 个有
- `AIO_Preprocessor` —— 3/14 个有
- `easy imageConcat` —— 2/14 个有
- `Krea2ControlApply` —— 1/14 个有
- `Krea2ControlImageEncode` —— 1/14 个有
- `Krea2ControlLoRALoader` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 14 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 14 | 84% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 43% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1280 | 504 - 1920 | 14 | 72% |
| 高度 | 720 | 512 - 1280 | 14 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，14 个样本，取值集中（一致性 84%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 504 - 1920，14 个样本
- 高度 中位数 720，观测区间 512 - 1280，14 个样本
- 高发问题（12/14 个样本）：Steps较低可能导致细节不足
