---
name: unknown_workflow_video_lora_sampler_241
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.793778
common_nodes: [BatchImagesNode, BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, CreateVideo, GetVideoComponents, KSamplerAdvanced, LoadImage, LoadVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, SaveVideo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy imageScaleDownToSize]
problems: []
missing: []
members: [数字人/数字人/视频局部重绘 人物替换，去字幕，风格转换 加速版 Bernini-贝尔尼尼_2062126637579329537.json, 数字人/数字人/视频编辑 物体替换，去水印字幕，风格转换等等多功能 Bernini贝尔尼尼 加速版_2062107326299070466.json, 视频生成/图生视频/Bernini贝尔尼尼高噪无加速版_2061860532604465153.json, 视频生成/图生视频/Bernini贝尔尼尼高噪无加速版（超牛动作迁移）_2062715583887663106.json, 视频生成/图生视频/服装新玩法-Bernini人物替换_2020633781832519681.json, 视频生成/图生视频/服装模特视频背景替换_2065039973153333250.json, 视频生成/图生视频/高噪无加速版_2062714987814146049.json, 视频生成/文生视频/Bernini-R 主体替换视频编辑流程_2062503702258348033.json, 视频生成/文生视频/Bernini-R 参考背景视频替换流程_2062503708742733826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_241

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/视频局部重绘 人物替换，去字幕，风格转换 加速版 Bernini-贝尔尼尼_2062126637579329537.json、数字人/数字人/视频编辑 物体替换，去水印字幕，风格转换等等多功能 Bernini贝尔尼尼 加速版_2062107326299070466.json、视频生成/图生视频/Bernini贝尔尼尼高噪无加速版_2061860532604465153.json、视频生成/图生视频/Bernini贝尔尼尼高噪无加速版（超牛动作迁移）_2062715583887663106.json、视频生成/图生视频/服装新玩法-Bernini人物替换_2020633781832519681.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
- `BatchImagesNode`
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `GetVideoComponents`
- `KSamplerAdvanced`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 8/9 个有
- `ImageFromBatch` —— 8/9 个有
- `RHLLMChatNode` —— 7/9 个有
- `Int` —— 5/9 个有
- `PrimitiveInt` —— 4/9 个有
- `SimpleMath+` —— 4/9 个有
- `StringReplace` —— 4/9 个有
- `Text` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `image_scale_pixel_v2` —— 4/9 个有
- `JjkText` —— 2/9 个有
- `TextCombinerTwo` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `TT_img_enc` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 78% |
| Prompt 约束强度(CFG) | 14 | 4 - 14 | 9 | 72% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 78%
- Prompt 约束强度(CFG) 中位数 14，观测区间 4 - 14，9 个样本
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
