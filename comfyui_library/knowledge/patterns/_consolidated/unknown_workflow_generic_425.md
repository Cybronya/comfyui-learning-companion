---
name: unknown_workflow_generic_425
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.814833
common_nodes: [PreviewAny, easy saveText, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/反推提示词/ComfyUI-llama-cpp_vlm 基础流_2006180240883720193.json, 图片生成/反推提示词/QWEN 3.5图像反推打标 lora训练助手_2044732074195689473.json, 图片生成/反推提示词/QWEN 3.5视频反推 Ai导演_2044346842959323137.json, 图片生成/反推提示词/【最强反推Qwen3.5】提示词扩写+图片反推+视频反推_2036679374207983618.json, 图片生成/反推提示词/【最强反推Qwen3.5】视频反推_2083739175047745537.json, 图片生成/反推提示词/视频提示词反推工作流地表最稳Video prompt word reverse inference_2065054598653632514.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_425

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/ComfyUI-llama-cpp_vlm 基础流_2006180240883720193.json、图片生成/反推提示词/QWEN 3.5图像反推打标 lora训练助手_2044732074195689473.json、图片生成/反推提示词/QWEN 3.5视频反推 Ai导演_2044346842959323137.json、图片生成/反推提示词/【最强反推Qwen3.5】提示词扩写+图片反推+视频反推_2036679374207983618.json、图片生成/反推提示词/【最强反推Qwen3.5】视频反推_2083739175047745537.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `PreviewAny`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `llama_cpp_parameters` —— 5/6 个有
- `GetVideoComponents` —— 4/6 个有
- `LoadVideo` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `TextInput_` —— 1/6 个有
- `workflow>qianwen` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
